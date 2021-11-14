X = [-2, -1, 3, 8]
p = [0.1, 0.5, 0.2, 0.2]

print("""Таблицей задан закон распределения дискретной случайной
величины Х. Найти математическое ожидание М(Х), дисперсию D(X) и
среднее квадратическое отклонение σ(X).""")

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
print(f"σ = sqrt({DX}) = {av_qu}")


