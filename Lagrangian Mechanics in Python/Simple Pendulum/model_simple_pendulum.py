# %%
# import statements
from sympy import *
from sympy.physics.mechanics import *

# enable LaTeX printing
init_vprinting()

# %%
# create symbolic variables
m, g, ell, t = symbols('m g ell t')
theta = dynamicsymbols('theta')

# define xm and ym
xm = ell*sin(theta)
ym = -ell*cos(theta)

# derivative
xm_dot = diff(xm, t)
ym_dot = diff(ym, t)

theta_dot = diff(theta, t)
theta_ddot = diff(theta_dot, t)

# Lagrangian
T = 1/2*m*(xm_dot**2 + ym_dot**2)
V = m*g*ym
L = T - V

# %% [markdown]
# $\dfrac{d}{dt} \bigg( \dfrac{\partial L}{\partial \dot \theta} \bigg) - \dfrac{\partial L}{\partial \theta} = 0$

# %%
# Euler-Lagrange Equation
eqn = diff ( diff(L, theta_dot), t) - diff(L, theta)

# Solution
sln = solve(eqn, theta_ddot)[0]
Eq(theta_ddot, sln)

# %%
# system of ODEs
x = Matrix([theta, theta_dot])
x_dot = diff(x, t)
Eq(x_dot, Matrix([theta_dot, sln]))


