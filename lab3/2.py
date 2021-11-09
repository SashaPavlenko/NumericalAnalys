import numpy as np
import sympy as sy
import pprint
import matplotlib.pyplot as plt
from lab3 import funcs

EPS = 1e-3
a, b = 0, 1

x = sy.Symbol('x')
f = x**3 +3*x**2 - 1

p, it = funcs.dichotomy(f, a, b, EPS, iter_num=True)

o = 3
print(f"f({round(p, o)}) = {f.subs(x, p).evalf()}\nThe number of iterations is {it}")

# s = sy.solveset(f, x, sy.Interval(2, 3))
# print(s)

pl = sy.plot(f, (x, -2.5, 2.5))