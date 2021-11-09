import numpy as np
import sympy as sy
import pprint
import matplotlib.pyplot as plt
from seminal_2 import final

TV = {
    't': [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
    'v': [5.848, 6.127, 6.300, 6.694, 7.047, 7.243, 7.368, 7.502],
}

N, (xN, yN) = final.Nuton(TV, retern_points=True)
dN = sy.diff(N)

x = sy.Symbol('x')
dN_points = [dN.subs(x, i) for i in TV['t']]

XY = {
    'x': [TV['t'][1], TV['t'][3], TV['t'][5]],
    'f': [TV['v'][1], TV['v'][3], TV['v'][5]],
    'df': ['', dN_points[3], ''],
}

E, (xE, yE) = final.Emita(XY, retern_points=True)

plt.plot(xN, yN)
plt.plot(xE, yE)
plt.plot(XY['x'], XY['f'], 'ro')

plt.xlim([XY['x'][0]-0.5, XY['x'][2]+0.5])
plt.ylim([6, 7.5])

plt.show()

