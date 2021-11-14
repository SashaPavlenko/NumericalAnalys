import math
import sympy as sy
from Anya.funcs import sy_func_to_lambda, fitFunc
import numpy as np

x = sy.Symbol('x')
t = sy.Symbol('t')

f = 1/sy.sqrt(2*sy.pi)*sy.Integral(sy.exp(-t*t/2), (t, 0, x)).doit()
# Интеграл верятностей Лапласа
PHI = lambda val: f.subs(x, val).evalf()

a, deviation, alpha, beta, delta = 15, 4, 15, 19, 1.5

out = f"""\
Условие задачи:
Диаметры деталей распределены по нормальному закону. Среднее
значение диаметра равно d мм, среднее квадратическое отклонение
{deviation} мм. Найти вероятность (P_1) того, что диаметр наудачу взятой детали
будет больше {alpha} мм и меньше {beta} мм; вероятность (P_2) того, что диаметр
детали отклонится от стандартной длины не более, чем на {delta} мм

Решение:
Пусть х - длина детали. Если случайная величина х распределена по нормальному 
закону, то вероятность ее попадания на отрезок [{alpha}; {beta}].

P(alpha < x < beta) = PHI((beta - a)/deviation) - PHI((alpha - a)/deviation)

P_1 = P({alpha} < x < {beta}) = PHI(({beta} - {a})/{deviation}) - PHI(({alpha} - {a})/{deviation}) = 
= PHI({(beta - a)/deviation}) - PHI({(alpha - a)/deviation}) = 
= {PHI((beta - a)/deviation)} - {PHI((alpha - a)/deviation)} \
= {PHI((beta - a)/deviation) - PHI((alpha - a)/deviation)}  

Вероятность отклонения длины детали от ее математического ожидания {a} не больше, 
чем на delta = {delta} мм, очевидно, что есть вероятность того, что длина детали попадает 
в интервал [{a} - {delta}; {a} + {delta}] и потому вычисляется также с помощью функции Лапласа:

P(a-delta < x < a+delta) = Φ(delta/deviation) - Φ(-delta/deviation)
P_2 = P({a}-{delta} < x < {a}+{delta}) = Φ({delta}/{deviation}) - Φ(-{delta}/{deviation}) =
= 2 * Φ({delta}/{deviation}) = 2*Φ({delta/deviation}) =  2*{PHI(delta/deviation)} =
= {2*PHI(delta/deviation)}
"""

print(out)

