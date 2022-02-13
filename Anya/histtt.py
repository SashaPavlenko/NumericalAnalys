# масло
# соев соус
# специи
# перемешать
# накрыть

import matplotlib.pyplot as plt
import numpy as np
import functools as ft

bins = 7
x = [31.2, 43.2, 55.2, 67.2, 79.2, 91.2, 103.2]
y = [0.03, 0.13, 0.15, 0.35, 0.2, 0.1, 0.04]




plt.hist(x, bins=bins,weights=y)

plt.show()

print([round(x[0]-(x[1]-x[0]), 1)] + x)
print(f"sorted y: {sorted(y, reverse=True)}")