# %%
import numpy as np
from scipy.integrate import solve_ivp

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# %%
# assign constants numerical values
g = 9.81
k = 40
m = 1
b = 1 # set to zero for no damping

# initial conditions: position = 0, velocity = 0
x0 = 0
x_dot0 = 0

# set the simulation time and frames per second
t_final = 10
fps = 30

# y[0] = x, y[1] = x_dot
def spring_mass_friction_ODE(t, y):
    return (y[1], g - k*y[0]/m - b*y[1]/m)

def spring_mass_ODE(t, y): 
    return (y[1], g - k*y[0]/m)

sol = solve_ivp(spring_mass_friction_ODE, [0, t_final], (x0, x_dot0), 
    t_eval=np.linspace(0,t_final,t_final*fps+1))

# output of the solver
x, x_dot = sol.y
t = sol.t

# %%
plt.plot(t, x, 'r', lw=2, label=r'$x$')
plt.plot(t, x_dot, 'b', lw=2, label=r'$\dot x$')
plt.title(f'Spring Mass System. k/m={k/m}, g={g}')
plt.legend()
plt.xlabel('Time (seconds)')
plt.ylabel(r'$x$ (m), $\dot x$ (m/s)')
plt.grid()
plt.show()

# %%
# animate theta, theta_dot vs time
fig, ax = plt.subplots()

x_curve, = ax.plot(t[0], x[0], 'r', lw=2, label=r'$x$')
x_dot_curve, = ax.plot(t[0], x_dot[0], 'b', lw=2, label=r'$\dot x$')

# make plot pretty
ax.set_title(f'Spring Mass System. k/m={k/m}, g={g}')
ax.set_xlim(0, t_final)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Time (seconds)')
ax.set_ylabel(r'$x$ (m), $\dot x$ (m/s)')
ax.legend(loc='lower left')
ax.grid()

def animate(i):
    x_curve.set_data(t[:i+1], x[:i+1])
    x_dot_curve.set_data(t[:i+1], x_dot[:i+1])

# save video @ 30 fps
ani = animation.FuncAnimation(fig, animate, frames=len(t))
ffmpeg_writer = animation.FFMpegWriter(fps=fps)
# ani.save('time_domain.mp4', writer=ffmpeg_writer)
ani.save('time_domain_with_friction.mp4', writer=ffmpeg_writer)

# %%
# phase diagram

plt.plot(x, x_dot, 'b', lw=2)
plt.title(f'Phase Diagram k/m={k/m}, g={g}')
plt.xlabel(r'Position $x$ (m)')
plt.ylabel(r'Velocity $\dot x$ (m/s)')
plt.grid()
plt.show()

# %%
# animate the phase diagram
fig, ax = plt.subplots()

phase_curve, = ax.plot(x[0], x_dot[0], 'b')
phase_dot, =  ax.plot(x[0], x_dot[0], 'ro')

ax.set_title('Spring Mass System - Phase Diagram')
ax.set_xlim(-0.01, 0.45)
ax.set_ylim(-1.2, 1.5)
ax.set_xlabel(r'$x$ (m)')
ax.set_ylabel(r'$\dot x$ (m/s)')
ax.grid()

def animate(i):
    phase_curve.set_data(x[:i+1], x_dot[:i+1])
    phase_dot.set_data([x[i]], [x_dot[i]])

ani = animation.FuncAnimation(fig, animate, frames=len(t))
ffmpeg_writer = animation.FFMpegWriter(fps=fps)
#ani.save('phase_diagram.mp4', writer=ffmpeg_writer)
ani.save('phase_diagram_with_friction.mp4', writer=ffmpeg_writer)


