import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.integrate import solve_ivp
import matplotlib.animation as animation
from matplotlib.transforms import Affine2D

#### Simulate the Spring Mass System ####
# assign constants
g = 9.81
k = 20
m = 1
b = 0.25

# initial conditions: position=-1, velocity=0
x0 = -1
x_dot0 = 0

# our system of differential equations
# y[0]=x, y[1]=x_dot
def spring_mass_ODE(t, y): 
    return (y[1], g - k*y[0]/m - b*y[1]/m)

# solve the ODE, evaluate at 30 fps
sol = solve_ivp(spring_mass_ODE, [0, 10], (x0, x_dot0), 
    t_eval=np.linspace(0,10,10*30))

# output of the solver
x, x_dot = sol.y
t = sol.t

#### Animate the Spring Mass ####
fig = plt.figure()
ax = fig.add_subplot(aspect='equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-5, 0)

# generate a spring with "n" interior points, starting at (0,0) and ending at (0,-1)
# spring has a width of 2/(2n)
def generate_spring(n):
    data = np.zeros((2,n+2)) # data = [x; y] is a long and skinny matrix (2 rows, many columns)
    data[:,-1] = [0,-1]
    for i in range(1,n+1):
        data[0,i] = -1/(2*n) if i % 2 else 1/(2*n)
        data[1,i] = -(2*i-1)/(2*n)
    return data

# put the (x,y) coordinates of the spring into a matrix
# append an array of 1s in the last row
data = np.append(generate_spring(30), np.ones((1,30+2)), axis=0)

# ell is the unstretch spring length
ell = 2          
y0 = -(ell + x0)
spring = Line2D(data[0,:], data[1,:], color='r')
circle = ax.add_patch(plt.Circle( (0,y0), 0.25, fc='b', zorder=3))
ax.add_line(spring)

# animate each frame "i"
def animate(i):
    y = -(ell + x[i])
    circle.set_center((0, y))

    # stretch the spring in the Y direction
    stretch_factor = -y
    
    # the 8 is an arbitrary scalar. feel free to change
    A = Affine2D().scale(8/stretch_factor, stretch_factor).get_matrix()
    data_new = np.matmul(A, data)

    # get the new x and y coordinates
    xn = data_new[0,:]
    yn = data_new[1,:]

    # update the spring
    spring.set_data(xn, yn)

# save a video: 30 fps
ani = animation.FuncAnimation(fig, animate, frames=len(t))
ffmpeg_writer = animation.FFMpegWriter(fps=30)
ani.save('spring_mass_affine.gif', writer=ffmpeg_writer)