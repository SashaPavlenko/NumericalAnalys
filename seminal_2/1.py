import sympy

from sympy import summation, product

# XY = [(-1, 4), (1, 2), (2, 7)]
XY = [(-1, -2), (1, 4), (2, 4)]
deg_pol = len(XY)



x = sympy.symbols('x')

# i = sympy.symbols('i')
# j = sympy.symbols('j')
# L = summation(XY[i][1] * product((x - XY[j][0])/(XY[i][0] - XY[j][0]), (j, 0, i - 1)) *
#               product((x - XY[j][0])/(XY[i][0] - XY[j][0]), (j, i+1, deg_pol)), (i, 0, deg_pol))

L = 0
for i in range(deg_pol):
    L_loc = 1
    for j in range(i):
        L_loc *= (x - XY[j][0])/(XY[i][0] - XY[j][0])
    for j in range(i+1, deg_pol):
        L_loc *= (x - XY[j][0])/(XY[i][0] - XY[j][0])
    L += XY[i][1]*L_loc

L = sympy.expand(L)
sympy.pprint(L)
