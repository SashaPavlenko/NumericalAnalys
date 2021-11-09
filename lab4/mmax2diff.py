import sympy as sy
import numpy as np
import math
from math import cos, sin
from sympy import sqrt, pprint
from lab3 import funcs
import matplotlib.pyplot as plt

omega = 11
AB = [
    (1.4, 3.),
    (0, math.pi),
    (0, math.pi),
]

F = [
    lambda x: sqrt(x*x+1)*cos(omega*x),
    lambda x: x,
    lambda x: 1,

]

EPS = 1E-4

index = 0
a, b = AB[index]
f = F[index]

x = sy.Symbol('x')
F = sy.sqrt(x*x + 1) * sy.cos(omega*x)
F = F.diff()
F = F.diff()
F = F.diff()
F = F.diff()

# F = F.diff()

F = abs(F)

# F_d_d = -x**2*cos(11*x)/(x**2 + 1)**(3/2) - 22*x*sin(11*x)/sqrt(x**2 + 1) - 121*sqrt(x**2 + 1)*cos(11*x) + cos(11*x)/sqrt(x**2 + 1)
# F = abs(F)

x_points = np.arange(a, b, 0.001)
y_points = list(map(lambda i: F.subs(x, i), x_points))

p = plt.plot(x_points, y_points)

# d2
# x_ans = 2.8636840820312495
# y_ans = F.subs(x, x_ans)

# d4
x_ans = 2.86876220703125
y_ans = F.subs(x, x_ans)
print(f"max|d^2(f)/dx^2| = {y_ans} for any x in [{a}; {b}]")

p2 = plt.plot(x_ans, y_ans, 'ro')

plt.grid()
plt.show()


# f = lambda x: 3*x**3*cos(11*x)/(x**2 + 1)**(5/2) + 33*x**2*sin(11*x)/(x**2 + 1)**(3/2) - 363*x*cos(11*x)/sqrt(x**2 + 1) \
#               - 3*x*cos(11*x)/(x**2 + 1)**(3/2) + 1331*sqrt(x**2 + 1)*sin(11*x) - 33*sin(11*x)/sqrt(x**2 + 1)
#
# x_ans = funcs.dichotomy(F, 2.8, 3.)
# print(x_ans)
