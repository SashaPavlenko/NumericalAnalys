import math
import sympy as sy

def sy_func_to_lambda(f):
    x = sy.Symbol('x')

    print(f)
    f = lambda y: f.subs(x, y)
    return f

def fitFunc(val, a, b, func_array):
    """

    :param val: значение функции или х_0
    :param a: левый конец отрезка
    :param b: правый конец отрезка
    :param func_array: функции (библиотеки sympy)
    :return: функцию библиотеки (sympy)
    """

    x = sy.Symbol('x')
    if val < a:
        return func_array[0]
    elif a <= val <= b:
        return func_array[1]
    else:
        return func_array[2]

def count_included_points(interval, points):
    """
    Count number of points that are in interval.
    :param interval: interval where we check points.
    :param points: array of points.
    :return: number of points that are in interval.
    """
    count = 0
    for i in points:
       if interval[0] <= i and i < interval[1]:
           # print(f"{interval[0]} <= {i} < {interval[1]}; \n{interval[0]} >= {i} and {i} < {interval[1]} = {interval[0] >= i and i < interval[1]}")
           count += 1
    return count

def dot_plus(l1, l2):
    s = ""
    for i in range(len(l1)):
        s += str(l1[i]) + "*" + str(l2[i])
        s += " + "

    s = s[:-1-1]

    return s

def s_mas(l):
    s = ""
    for i in range(len(l)):
        s += str(l[i])
        s += " + "

    s = s[:-1 - 1]

    return s
