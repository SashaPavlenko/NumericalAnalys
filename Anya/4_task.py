X = [-2, 2, 3, 8]
p = [0.1, 0.1, 0.3, 0.5]

MX = 0
for i in range(len(X)):
    MX += X[i]*p[i]
    print(f"{X[i]}*{p[i]} + ", end="")

print(f"= M(X) = {MX}")

MXX = 0
for i in range(len(X)):
    MXX += X[i]**2*p[i]
    print(f"{X[i]**2}*{p[i]} + ", end="")

print(f"= M(X^2) = {MXX}")

DX = MXX - MX**2
av_qu = DX**0.5

print(f"DX = M(X^2) - (MX)^2 = {MXX} - {(MX)**2} = {DX}")
print(f"av_qu = sqrt({DX}) = {av_qu}")


