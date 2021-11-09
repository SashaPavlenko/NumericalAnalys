# a, b, n, f
from math import log

def int_rect(f, n, a, b):
    h = (b - a) / n
    x_i = lambda i: a + i*h

    ssum = 0
    for k in range(n):
        ssum += f( (x_i(k) + x_i(k+1)) /2 )

    ssum *= h
    return ssum

def trapez(f, n, a, b):
    h = (b - a) / n
    x_i = lambda i: a + i * h

    ssum = f(x_i(0)) + f(x_i(n))
    for k in range(1, n):
        ssum += 2 * f(x_i(k))

    ssum *= h / 2
    return ssum


def Simpson(f, n, a, b):
    h = (b - a) / n
    m = n // 2
    x_i = lambda i: a + i * h

    ssum = f(x_i(0)) + f(x_i(n)) + 4*f( x_i(2*m-1) )
    for k in range(1, m):
        # print(f"2k = {2*k}; 2k-1 = {2*k-1}; k = {k}")
        ssum += 4*f( x_i(2*k-1) ) + 2 * f( x_i(2*k) )

    ssum *= h / 3
    return ssum

def Runge(a, b, n0, EPS, f, f_int):
    """
    :param a: начало отрезка
    :param b: конец отрезка
    :param n0: начальное число точек разбиения n0
    :param EPS: точность
    :param f: подынтегральная функция
    :param C: числовая константа
    :param f_int: функция интегрирования
    :return: искомое число разбиений n
    """
    n = n0
    f_name = f_int.__name__
    C = 1/15 if (f_name == "Simpson") else 1/3

    while abs(f_int(f, 2*n, a, b) - f_int(f, n, a, b)) > C*EPS:
        n = 2*n

    return n


def exac_loss(a, b, n0, EPS, f, f_int):
    d2max = 367.431584696282
    d4max = 44720.5823854075
    h = (b-a) / n0

    s = f_int.__name__
    if s == "int_rect":
        C = 1/24
        df = d2max
        delta = (b-a)**3
        f_n = lambda n: n**2

    elif s == "trapez":
        C = 1/12
        df = d2max
        delta = (b-a)**3
        f_n = lambda n: n**2

    elif s == "Simpson":
        C = 1/180
        df = d4max
        delta = (b-a)**5
        f_n = lambda n: n**4

    else:
        raise Exception("ERROR")

    E = df * C / EPS * delta

    while f_n(n0) < E:
        if n0 > 20:
            n0 += n0 // 7
        else:
            n0 *= 2

    return n0