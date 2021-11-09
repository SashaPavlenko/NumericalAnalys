import sympy
import numpy
# import matplotlib

X = [-2, 0, 2]
x_star = 1

x = sympy.symbols('x')
f = abs(sympy.diff(sympy.cosh(x), x, 3))

# sympy.plot(f, (x, -2.5, 2.5))

mmax = f.subs(x, 2).evalf()
fac = sympy.factorial(len(X))

i = sympy.symbols('i')
p = 1
for i in range(len(X)):
    p *= x_star - X[i]
p = abs(p)

R = mmax * p / fac

print(R)
print(1/2*sympy.sinh(2).evalf())
