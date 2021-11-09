import sympy as sy
from seminal_2 import final

XY = {
    'x': [1, 2, 3],
    'f': [15, 29, 55],
    'df': ['', 19, ''],
}

l = final.Emita(XY, divided_differenses=True)
N = final.Emita(XY)

print(l)

sy.pprint(N)