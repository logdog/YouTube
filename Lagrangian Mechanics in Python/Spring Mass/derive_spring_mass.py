# %%
from sympy import *
from sympy.physics.mechanics import *
init_vprinting()

# %%
# define symbols
m, g, k, t = symbols('m g k t')
x = dynamicsymbols('x')

# take derivatives
x_dot = diff(x, t)
x_ddot = diff(x_dot, t)

# Lagrangian
T = 1/2*m*x_dot**2
V = -m*g*x + 1/2*k*x**2
L = T - V

# solve Euler-Lagrange
eqn = diff( diff(L, x_dot), t) - diff(L, x)
sln = solve(eqn, x_ddot)[0]
Eq(x_ddot, sln)


