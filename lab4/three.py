import sympy as sy
import math
from sympy import cos, sqrt, pprint
from lab4 import funcs

x = sy.Symbol('x')



a, b = 0, 2
EPS = 1e-4
p = -1

x_equil = a
f = sy.sin(x)/x

eq = x**p
P = sy.sin(x)


psi = P.series(x, x0=x_equil, n=8).removeO()

g = P.series(x, x0=x_equil, n=4).removeO()
phi = psi - g

g, phi = g*(x-x_equil)**p, phi*(x-x_equil)**p
g, phi = g.simplify(), phi.simplify()

# print("g(x) = ", end="")
# sy.pprint(g)
# print("phi(x) = ", end="")
# sy.pprint(phi)

f_int = funcs.Simpson

n1 = funcs.Runge(a, b, 1, EPS, lambda val: g.subs(x, val), f_int)
n2 = funcs.Runge(a, b, 1, EPS, lambda val: phi.subs(x, val), f_int)
# int_rect: n1 = 256, n2 = 256
# trapez: n1 = 512, n2 = 512
# Simpson: n1 = 16, n2 = 16

I1 = f_int(lambda val: g.subs(x, val), n1, a, b)
I2 = f_int(lambda val: phi.subs(x, val), n2, a, b)

res = (I1+I2).evalf()

print(f"Answer: {res}\nObservational error: {'%e' %(abs(res - 1.60541297680269))}")