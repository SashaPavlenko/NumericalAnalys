import numpy as np
import sympy as sy
import pprint
import matplotlib.pyplot as plt

def get_x(l, n):
    x = sy.Symbol('x')
    prod = 1
    for i in range(n):
        prod *= x - l[i][0]
    return prod

XY = {
    'x': [1, 2, 3],
    'f': [15, 29, 55],
    'df': ['', 19, ''],
}

LenXY = len(XY['x'])

# Строим матрицу первичных/вторичных/... разностей.
# Создаем матрицу из нулей размерности [количество точек; 2 (координаты по t и v) + количество точек - 1].
l = np.zeros((LenXY, 1 + LenXY))
l = l.transpose()

# Заносим в первый столбец координаты по t, в второй по v.
l[0] = XY['x']
l[1] = XY['f']
l = l.transpose()

l = np.vstack((l, np.array([[0, 0, 0, 0]])))
l = np.hstack((l, np.array([[0, 0, 0, 0]]).transpose()))

l[[2, 3]] = l[[3, 2]]
l[2][0] = XY['x'][1]
l[2][1] = XY['f'][1]

LenXY = l.shape[0]
EPS = 1e-6

for j in range(2, LenXY+1):
    for i in range(LenXY - j+1):  # range(LenTV-1 -j+1)
        if j-1 == 1 and abs(l[i+1][0] - l[i][0]) < EPS:
            l[i][j] = XY['df'][i]
        else:
            l[i][j] = round(l[i+1][j-1] - l[i][j-1], 4) / (l[i+j - 1][0] - l[i][0])

# pprint.pprint(l)

x = sy.symbols('x')
N = 0
n = sy.symbols('n')
for i in range(1, l.shape[1]):
    y = l[0][i]
    N += y * get_x(l, i-1)
    print(get_x(l, i-1))

N = sy.simplify(N)

sy.pprint(N)

p1 = plt.plot(XY['x'], XY['f'], 'ro')

x_points = np.arange(0.5, 3.5, 0.1)
y_points = list(map(lambda i: N.subs(x, i), x_points))
p2 = plt.plot(x_points, y_points)

# p3 = plt.plot(x_star, N.subs(x, x_star), '*', markersize=20)

plt.show()
