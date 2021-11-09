import math
import sympy as sy
from Anya.funcs import sy_func_to_lambda, fitFunc
import numpy as np


x = sy.Symbol('x')
a, b = -0.5, 0.5
const = lambda val: (x*1).subs(x, val)

F_int = [
    const(0),
    x+1/2,
    const(1),
]

F_diff = list(map(lambda f: f.diff(), F_int))

f = lambda val: fitFunc(val, a, b, F_diff).subs(x, val)

MX = (a+b)/2
DX = (b-a)**2/12
s_deviation = DX**0.5

out_int = """\
Интегральная функция
{F[0]}, x < {a}
{F[1]}, {a} <= x <= {b}
{F[2]}, x > {b}
""".format(F=F_int, a=a, b=b)

out_diff = """\
Дифференциальная функция
{F[0]}, x < {a}
{F[1]}, {a} <= x <= {b}
{F[2]}, x > {b}
""".format(F=F_diff, a=a, b=b)

print(out_int, out_diff, sep="\n")

print(f"M(X) = ({a} + {b}) / 2 = {MX}")
print(f"D(X) = ({b} - {a})^2/12 = {DX}")
print(f"standart_deviation = sqrt({DX}) = {s_deviation}")