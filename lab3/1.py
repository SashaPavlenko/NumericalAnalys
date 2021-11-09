import numpy as np
import sympy as sy
import pprint
import matplotlib.pyplot as plt
from lab3 import funcs

EPS = 1e-5
a, b = 2, 3

x = sy.Symbol('x')
f = x**2 * sy.cos(2*x) + 1

p, it = funcs.secant(f, a, b, EPS, iter_num=True)

o = 5
print(f"f({round(p, o)}) = {f.subs(x, p).evalf()}\nThe number of iterations is {it}")

# s = sy.solveset(f, x, sy.Interval(2, 3))
# print(s)

sy.plot(f, (x, 1.8, 3.2))

