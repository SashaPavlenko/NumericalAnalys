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
