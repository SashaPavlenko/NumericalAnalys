import math
import sympy as sy
import numpy as np
from Anya.funcs import count_included_points as count_pts, dot_plus, s_mas

num_of_var = int(input("Введите номер варианта: "))
with open(f"7_tasks/{num_of_var} вариант/данные.txt", "r") as f:
    s = f.read()


l = s.replace("\n", " ").replace(", ", ".").replace(",", ".").split()
l = list(map(float, l))

if len(l) != 100:
    raise Exception("IncorrectData")

l = np.array(l)

l_copy = l.copy().reshape(10,10)
l.sort()

n_len = l.shape[0]
xmin = l.min()
xmax = l.max()

N = n_len
R = l.max() - l.min()
k = 1 + math.floor(3.222 * math.log10(n_len))
h = math.ceil(R / k)
a_0 = xmin
a_i = lambda i: a_0 + i*h

intervals = []
# (a_i-1, a_i)
for i in range(1, k+1):
    intervals.append( (a_i(i-1), a_i(i)) )

int_copy = intervals.copy()


# [a_i-1; a_i)
intervals = list(map(lambda x: str(x), intervals))
intervals = list(map(lambda x: "[" + x[1:], intervals))
s_intervals = "; ".join(intervals).replace(",", ";")

ni = [count_pts(i, l) for i in int_copy]
n = [100 for i in int_copy]
wi = [ni[i]/n[i] for i in range(len(int_copy))]

mmat_pic_1 = np.array([intervals, ni, n, wi])

xi_for_pic_2 = [(i[0] + i[1])/2 for i in int_copy]
xi_for_pic_2[-1] = round(xi_for_pic_2[-1], 3)

mmat_pic_2 = np.array([xi_for_pic_2, ni, n, wi])
s_mmat_2 = np.array([xi_for_pic_2, ni, n, wi], dtype=str)

d = mmat_pic_1[3]
d = np.array(list(map(float, d.tolist())))

x_sred = np.sum(d * mmat_pic_2[0])

x_i = mmat_pic_2[0]
ssum = 0
ss = ""
for i in range(len(x_i)):
    ssum += (x_i[i] - x_sred)**2*d[i]
    ss += f"({x_i[i]} - {x_sred})^2*{d[i]} + "

ss = ss[:-1-1]

D = ssum
squadr = n_len / (n_len-1) * D
out = f"""\
Исходная таблица
{l_copy}

Решение:
- Составим интервальное распределение выборки

Выстроим в порядке возрастания, имеющиеся у нас значения
{l.reshape(10,10)}

Шаг 1. Найти размах вариации 
R = x_(max) - x_(min)

определим максимальное и минимальное значение имеющихся значений: х_(min) = {l.min()}; х_(max) = {l.max()}
R = х_(max) - х_(min) = {l.max()} - {l.min()} = {l.max() - l.min()}

Шаг 2. Найти оптимальное количество интервалов
Скобка ⌊ ⌋ означает целую часть (округление вниз до целого числа).

k = 1 + ⌊3,222 * lg(N) ⌋
k = 1 + ⌊3,222 * lg({n_len}) ⌋ = 1 + ⌊{3.222 * math.log10(n_len)}⌋ = 1 + {math.floor(3.222 * math.log10(n_len))} = {k} 

Шаг 3. Найти шаг интервального ряда 
Скобка ⌈ ⌉ означает округление вверх, в данном случае не обязательно до целого числа
h = ⌈ R/k ⌉ = ⌈ {R}/{k} ⌉ = ⌈ {R / k} ⌉ = {h} 

Шаг 4. Найти узлы ряда:
a_0 = x_(min) = {xmin}
a_(i) = a_0 + i*h = {a_0} + i*{h}, i = 1, ..., {k}

Заметим, что поскольку шаг h находится с округлением вверх, последний узел a_(k) >= x_(max)

[a_(i-1); a_(i)): {s_intervals}

- построим гистограмму относительных частот;
Найти частоты f_(i) – число попаданий значений признака в каждый из интервалов [a_(i-1), a_(i))
f_(i) = n_(i), n_(i) - количество точек на интервале [a_(i-1); a_(i))

Относительная частота интервала [a_(i-1);a_(i)) - это отношение частоты f_(i) к общему количеству исходов:
w_(i) = f_i/{N}, i = 1, ..., {k}

Названия строк по номерам (вписать в таблице)
[a_(i-1); a_(i))
n_(i)
n
w_(i)

Вадим, запускай код через python console и в SciView и там выбираем Data и вводим mmat_pic_1  
{mmat_pic_1}

Вадим, рисуем гистограмму с этими значениями 
x = {list(map(lambda x: x[1],int_copy))}
y = {list(map(lambda x: float(x), mmat_pic_1[3]))}

- Перейдем от составленного интервального распределения к точечному выборочному распределению, взяв за значение признака \
середины частичных интервалов.

Названия строк по номерам (вписать в таблице)
x_i
n_i
n
w_i

{s_mmat_2}

- Построим полигон относительных частот и найдем эмпирическую функцию распределения, построим ее график:
Полигон относительных частот интервального ряда – это ломаная, соединяющая точки (x_i,w_i), где x_i - середины интервалов: 
x_i = (a_(i-1)+a_i )/2, i = 1, ..., {k}

*Построй в файле pictures.py график интервального распределения и нарисуй на бумаге! 
x = {list(map(lambda x: float(x),mmat_pic_2[0]))}
y = {list(map(lambda x: float(x), mmat_pic_1[3]))}


- найдем эмпирическую функцию распределения и построим ее график;
n = {n_len}
n_x = {list(map(lambda x: int(x), mmat_pic_2[1].tolist()))}
x_i = {mmat_pic_2[0].tolist()}

Вставь скриншот определения эмперической функции (Форм_эмп_ф.jpg) 

Зайди в emperich.py и перепиши чему равен F(x)
Вставить график эмперической функции (переписать рис.2)

Читай крч с задачи
- вычислим все точечные статистические оценки числовых характеристик
признака: среднее X̅; выборочную дисперсию и исправленную
выборочную дисперсию; выборочное с.к.о. и исправленное выборочное с.к.о. s; 

X̅ = ∑_(i=1)^{mmat_pic_1[0].shape[0]}▒(w_i*x_i) = {dot_plus(mmat_pic_1[3], mmat_pic_2[0])} = 
= {s_mas(d * mmat_pic_2[0])} =
= {np.sum(d * mmat_pic_2[0])}

Выборочная средняя: 
X_ср = ∑_(i=1)^{mmat_pic_1[0].shape[0]}▒(x_i*w_i) = {x_sred}

Выборочная дисперсия:
D = ∑_(i=1)^{mmat_pic_1[0].shape[0]}▒(x_i - X_cp)^2*w_i =
= {ss} = 
= {D}

Исправленная выборочная дисперсия
S^2 = N/(N-1)*D = {n_len}/({n_len-1}) * {D} ≈ {squadr}

Выборочное среднее квадратичное отклонение:
σ = √(D) = √({D}) ≈ {D**0.5}

исправленное выборочное с.к.о s
s = √(S^2) ≈ √({squadr}) ≈ {squadr**0.5}

- считая первый столбец таблицы выборкой значений признака Х, а второй -
выборкой значений Y, оценить тесноту линейной корреляционной
зависимости между признаками и составить выборочное уравнение прямой
регрессии Y на Х 
"""


X = l_copy[0]
Y = l_copy[1]

# Тест, корреляц что-то там равно ~0.565
# X = [10.0, 10.0, 10.1, 10.2, 10.8, 11.0, 11.1, 11.3, 11.3, 11.4, 11.8, 12.0, 12.0, 12.1, 12.3, 13.0, 13.4, 13.5, 14.5, 15.6]
# Y = [0.7, 0.7, 0.65, 0.61, 0.73, 0.65, 0.65, 0.75, 0.7, 0.7, 0.69, 0.72, 0.6, 0.75, 0.63, 0.8, 0.78, 0.7, 0.7, 0.85]
# X = [2, 2.5, 3, 3.5, 4]
# Y = [1.25, 1.45, 1.65, 1.85, 2.05]
# X = np.array(X)
# Y = np.array(Y)


l3 = np.zeros((5, X.shape[0]))
l3[0] = X
l3[1] = Y
l3[2] = X*Y
l3[3] = X*X
l3[4] = Y*Y

l3 = list(map(lambda x: x+[np.sum(x)], l3.tolist()))
l3 = np.array(l3).transpose()


X_N = X.shape[0]
mas = lambda k: l3[X_N][k]

res = (mas(2)/X_N - mas(0)/X_N * mas(1)/X_N) / ((mas(3)/X_N - (mas(0)/X_N)**2)**0.5 * (mas(4)/X_N - (mas(1)/X_N)**2)**0.5)

v1 = 1/X_N*mas(0)
v2 = 1/X_N*mas(1)

v3qu = (mas(3)/X_N - (mas(0)/X_N)**2)
v4qu = (mas(4)/X_N - (mas(1)/X_N)**2)

v3 = v3qu**0.5
v4 = v4qu**0.5

v5 = 1/X_N*mas(2) - mas(0)*mas(1)

out += f"""
X = {l_copy[0]}
Y = {l_copy[1]}

Столбцы:
1. x_i
2. y_i
3. x_i*y_i
4. x_i^2
5. y_i^2

Последняя строчка - сумма всех элементов над ней 

1) Оценить тесноту линейной корреляционной зависимости между признаками

*Запусти программу в python console и посмотри массив l в спец. окне
Подпиши все строки/столбцы, которые указаны сверху.

*Переписать дальше все, что Формула_корреляц.png
продольжение равно:

({mas(2)}/{X_N} - {mas(0)}/{X_N} * {mas(1)}/{X_N})/(√({mas(3)}/{X_N} - \
({mas(0)}/{X_N})^2) * √({mas(4)}/{X_N} - ({mas(1)}/{X_N})^2)) = \
{res}

2) Cоставим выборочное уравнение прямой регрессии Y на Х

*Переписать дальше все, что Формула_корреляц.png и подставить в неё v1-v5
v1 = {v1}
v2 = {v2}
v3 = {v3}
v4 = {v4}
v5 = {v5}

v3qu = {v3qu}
v4qu = {v4qu}

{round(v1, 4)}
{round(v2, 4)}
{round(v3qu, 4)} {round(v3, 4)}
{round(v4qu, 4)} {round(v4, 4)}
{round(v5, 4)}

y_x = { round(res*v4/v3, 4) } * x + { round(v2 - v1*res*v4/v3, 4) }
r_xy = {round(res, 4)}

"""

print(out)
