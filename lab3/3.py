import numpy as np
import sympy as sy
import pprint
import matplotlib.pyplot as plt
from lab3 import funcs

a, b = 2.7, 2.9

x = sy.Symbol('x')
f = x**2 * sy.exp(x) - 130
phi = sy.log(130 / x**2)

# sy.plot(phi, (x, a, b))
# sy.plot(f, (x, 0, 2.9))

# sy.pprint(phi)

p, it = funcs.fixed_point_iteration(phi, a, b, eps=1e-8, iter_num=True)
o = 6
print(f"f({round(p, o)}) = {f.subs(x, p).evalf()}\nThe number of iterations is {it}")

print(f"|x_delta - x*| = {abs(2.80484085096985 - p)}")