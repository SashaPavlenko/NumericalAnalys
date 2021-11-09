import numpy as np
import sympy as sy
import pprint
import matplotlib.pyplot as plt

TV = {
    't': np.arange(1.5, 5.5, 0.5),
    'v': np.array([5.848, 6.127, 6.300, 6.694, 7.047, 7.243, 7.368, 7.502]),
}


x_star = 3.34
LenTV = len(TV['t'])

# Строим матрицу первичных/вторичных/... разностей.
# Создаем матрицу из нулей размерности [количество точек; 2 (координаты по t и v) + количество точек - 1].
l = np.zeros((LenTV, 1 + LenTV))
l = l.transpose()

# Заносим в первый столбец координаты по t, в второй по v.
l[0] = TV['t']
l[1] = TV['v']
l = l.transpose()

for j in range(2, LenTV+1):
    for i in range(LenTV - j+1):  # range(LenTV-1 -j+1)
        l[i][j] = round(l[i+1][j-1] - l[i][j-1], 4)
# Матрица первичных/вторичных/... разностей построена.

x = sy.symbols('x')
h = l[1][0] - l[0][0]
t = (x - l[-1][0]) / h

# pprint.pprint(l.tolist())

N = 0
n = sy.symbols('n')
for i in range(LenTV):
    y = l[LenTV - i - 1][i + 1]
    N += y * sy.product(t + n, (n, 0, i-1)) / sy.factorial(i)

N = sy.simplify(N)

p1 = plt.plot(TV['t'], TV['v'], 'ro')

x_points = np.arange(1.3, 5.2, 0.1)
y_points = list(map(lambda i: N.subs(x, i), x_points))
p2 = plt.plot(x_points, y_points)

p3 = plt.plot(x_star, N.subs(x, x_star), '*', markersize=20)

plt.show()