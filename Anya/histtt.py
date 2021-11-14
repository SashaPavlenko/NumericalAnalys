# масло
# соев соус
# специи
# перемешать
# накрыть

import matplotlib.pyplot as plt
import numpy as np
import functools as ft

x = [19.2, 31.2, 43.2, 55.2, 67.2, 79.2, 91.2]
y = [0.04, 0.13, 0.16, 0.34, 0.2, 0.09, 0.03]

plt.hist(x, weights=y)

plt.show()