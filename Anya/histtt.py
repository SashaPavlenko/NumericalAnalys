# масло
# соев соус
# специи
# перемешать
# накрыть

import matplotlib.pyplot as plt
import numpy as np
import functools as ft

bins = 7
x = [28.5, 40.5, 52.5, 64.5, 76.5, 88.5, 100.5]
y = [0.07, 0.15, 0.21, 0.33, 0.15, 0.07, 0.02]

plt.hist(x, bins=bins,weights=y)

plt.show()

print([x[0]-(x[1]-x[0])]+x)
print(f"sorted y: {sorted(y)}")