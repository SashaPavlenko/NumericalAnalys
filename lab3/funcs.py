import numpy as np
import sympy as sy
import pprint
import matplotlib.pyplot as plt


def secant(f, a, b, eps=1e-5, iter_num=False):
    # Stage 2.
    x0 = a
    x1 = b

    x = sy.Symbol('x')
    func = lambda val: f.subs(x, val).evalf()

    it = 1
    # Stage 4.
    x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
    s = lambda x0, x1, x2: f"x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0)) \n\
    = {x1} - (func({x1}) * ({x1} - {x0})) / (func({x1}) - func({x0})) \n\
    = {x1} - ({func(x1) * (x1 - x0)}) / ({func(x1) - func(x0)}) = {x2}\n"
    print(s(x0, x1, x2))

    while abs(func(x2)) > eps:
        # Stage 5.1.
        print(f"cond: abs(func({x2})) = {abs(func(x2))} > {eps}")
        print(f"func(x0) * func(x2) < 0\n{func(x0)} * {func(x2)} = {func(x0) * func(x2)} < 0\n")
        if func(x0) * func(x2) < 0:
            x1 = x2
            print(f"x1 = x2 = {x2}")
        else:
            x0 = x2
            print(f"x0 = x2 = {x2}")

        it += 1

        # Stage 5.2.
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        print(s(x0, x1, x2))

    x_star = x2
    if iter_num:
        return x_star, it
    else:
        return x_star


def dichotomy(f, a, b, eps=1e-5, iter_num=False):
    x = sy.Symbol('x')
    func = lambda val: f.subs(x, val).evalf()

    it = 0
    c = (a + b) / 2

    while abs(b - a) > 2*eps:
        c = (a + b) / 2

        t1, t2 = func(a), func(c)
        if t1*t2 < 0:
            b = c
        elif t1*t2 > 0:
            a = c
        else:
            a = b

        it += 1

    x_star = c
    if iter_num:
        return x_star, it
    else:
        return x_star

def fixed_point_iteration(phi, a, b, eps=1e-5, iter_num=False):
    x0 = a + 0.1
    x = sy.Symbol('x')

    phi_d = phi.diff()
    phi_d = abs(phi_d)
    q = phi_d.subs(x, a)
    q_eps = ((1 - q) / q) * eps

    phi_f = lambda val: phi.subs(x, val)
    x1 = phi_f(x0)

    it = 1
    while abs(x1 - x0) >= q_eps:
        x0 = x1
        x1 = phi_f(x0)
        it += 1

    x_star = x1
    if iter_num:
        return x_star, it
    else:
        return x_star