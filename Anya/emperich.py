import matplotlib.pyplot as plt
import numpy as np
import functools as ft

n = 100
n_x= [4,13,16,34,20,9,3]
x_i= [13.2,25.2,37.2,49.2,61.2,73.2,85.2]


ccount = 0
out = "F(x) = \n"

val = 0 / n
out += f"{val}, x <= {x_i[0]}, \n"
y = [0]

for i in range(len(n_x)-1):
    val = ft.reduce(lambda x, y: x+y, n_x[:i+1]) / n
    out += f"{val}, {x_i[i]} <= x <= {x_i[i+1]}, \n"
    y.append(val)

i = len(n_x)-1
val = ft.reduce(lambda x, y: x+y, n_x[:i+1]) / n
out += f"{val}, x > {x_i[i]}; \n"
y.append(val)

x_i = [x_i[0]-5] + x_i

print(out)

p1 = plt.plot(x_i, y, '-go')
plt.grid(axis="y")
plt.savefig('рис2.png')
plt.show()