import sympy as sy
import math
from sympy import cos, sqrt, pprint
from lab4 import funcs


x = sy.Symbol('x')

f = 2**0.5*sy.log(abs(x* + sqrt(x**x+4)))
# f = lambda x: 1/(2+0.5*x*x)**0.5

sy.pprint((f.subs(x, 1.2) - f.subs(x, 0.4)).evalf)
print((sqrt(2)*(math.log(1.2+sqrt(1.2*1.2+4))-math.log(0.4+sqrt(0.4*0.4+4)))).evalf())
#
# print(funcs.trapez(f, 4, 0.4, 1.2))