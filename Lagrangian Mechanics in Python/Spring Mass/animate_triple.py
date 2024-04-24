# Create Triple animated plot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.integrate import solve_ivp
import matplotlib.gridspec as gridspec
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

# set the simulation time and frames per second
t_final = 10
fps = 30

# our system of differential equations
# y[0]=x, y[1]=x_dot
def spring_mass_ODE(t, y): 
    return (y[1], g - k*y[0]/m - b*y[1]/m)

# solve the ODE, evaluate at 30 fps
sol = solve_ivp(spring_mass_ODE, [0, t_final], (x0, x_dot0), 
    t_eval=np.linspace(0,t_final,t_final*fps+1))

# output of the solver
x, x_dot = sol.y
t = sol.t

#### Animate the System ####
fig = plt.figure()
gs = gridspec.GridSpec(2,2, width_ratios=[1,1], height_ratios=[1,1])

# theta, theta_dot vs time
ax0 = fig.add_subplot(gs[0,0])
ax0.set_xlim(0, max(t))
ax0.set_ylim(-6.25, 7)
ax0.grid()
ax0.set_yticklabels([])
ax0.set_xticklabels([])

x_curve, = ax0.plot(t[0], x[0], 'r', label=r'$x$')
x_dot_curve, = ax0.plot(t[0], x_dot[0], 'b', label=r'$\dot x$')

# phase diagram
ax1 = fig.add_subplot(gs[1,0])
ax1.set_xlim(-1.1, 2.1)
ax1.set_ylim(-6.25, 7)
ax1.grid()
ax1.set_yticklabels([])
ax1.set_xticklabels([])

phase_curve, = ax1.plot(x[0], x_dot[0], 'b')
phase_dot, =  ax1.plot(x[0], x_dot[0], 'ro')

################## mass spring animation

ax2 = fig.add_subplot(gs[:,1])
ax2.axis('equal')
ax2.set_xlim(-1.25, 1.25)
ax2.set_ylim(-5.5, 0.5)
ax2.set_yticklabels([])
ax2.set_xticklabels([])

# generate a spring with "n" interior points, starting at (0,0) and ending at (0,-1)
# spring has a width of 2/(2n)
def generate_spring(n):
    data = np.zeros((2,n+2))
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
circle = ax2.add_patch(plt.Circle( (0,y0), 0.2, fc='b', zorder=3))
ax2.add_line(spring)

def animate(i):
    x_curve.set_data(t[:i+1], x[:i+1])
    x_dot_curve.set_data(t[:i+1], x_dot[:i+1])

    phase_curve.set_data(x[:i+1], x_dot[:i+1])
    phase_dot.set_data([x[i]], [x_dot[i]])

    y = -(ell + x[i])
    circle.set_center((0, y))

    # stretch the spring in the Y direction
    stretch_factor = ell + x[i]
    
    A = Affine2D().scale(8/stretch_factor, stretch_factor).get_matrix()
    data_new = np.matmul(A, data)

    # get the new x and y coordinates
    xn = data_new[0,:]
    yn = data_new[1,:]

    # update the spring
    spring.set_data(xn, yn)

# save a video: 30 fps
ani = animation.FuncAnimation(fig, animate, frames=len(t))
ffmpeg_writer = animation.FFMpegWriter(fps=fps)
ani.save('all.gif', writer=ffmpeg_writer)