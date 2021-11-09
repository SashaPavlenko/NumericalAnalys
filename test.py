import math

p = 0.6
q = 0.4
n = 7
k = 5

f = lambda n, k: math.comb(n, k) * p**k* q**(n-k)


print(f(7, 5))
s = 0

for k in range(5):
    print(f"P_7({k}) = {f(7, k)}")
    s += f(7, k)

print(s)
