import matplotlib.pyplot as plt
import numpy as np


n_bins = 20

x = [25.2, 37.2, 49.2, 61.2, 73.2, 85.2, 97.2]
y = [0.03, 0.13, 0.15, 0.35, 0.2, 0.1, 0.04]

p1 = plt.plot(x, y, '-go')
# plt.grid(axis="y")
# plt.savefig('рис1.png')
plt.show()

print(" ".join(list(map(str, x))))
print(f"sorted y: {sorted(y, reverse=True)}")