import matplotlib.pyplot as plt
import numpy as np


n_bins = 20

x = [22.5, 34.5, 46.5, 58.5, 70.5, 82.5, 94.5]
y = [0.07, 0.15, 0.21, 0.33, 0.15, 0.07, 0.02]



p1 = plt.plot(x, y, '-go')
# plt.grid(axis="y")
# plt.savefig('рис1.png')
plt.show()

print(" ".join(list(map(str, x))))
