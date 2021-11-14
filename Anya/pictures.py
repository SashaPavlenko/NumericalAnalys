import matplotlib.pyplot as plt
import numpy as np


n_bins = 20

x = [13.2, 25.2, 37.2, 49.2, 61.2, 73.2, 85.2]
y = [0.04, 0.13, 0.16, 0.34, 0.2, 0.09, 0.03]



p1 = plt.plot(x, y, '-go')
plt.grid(axis="y")
# plt.savefig('рис1.png')
plt.show()
