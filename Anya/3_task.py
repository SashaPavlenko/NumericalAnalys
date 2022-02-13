import math


# Данные 5 2 1 3

p = 0.3
n = 5
k = 2
k1 = 1
k2 = 3

q = 1 - p

# f(k) = C_n^k * p^k * q^(n-k) - событие появится ровно k раз
f = lambda n, k: math.comb(n, k) * p**k* q**(n-k)

P_n = lambda k: f(n, k)

# В задании б) 2 случая
out_1_k_1 = ""
sum_1_k_1 = 0
for i in range(k):
    out_1_k_1 += str(P_n(i)) + " + "
    sum_1_k_1 += P_n(i)

out_1_k_1 = out_1_k_1[:-2]

out_k_n = ""
sum_k_n = 0
for i in range(k, n+1):
    out_k_n += str(P_n(i)) + " + "
    sum_k_n += P_n(i)

out_k_n = out_k_n[:-2]

# В задании в)
out_k1_k2 = ""
sum_k1_k2 = 0
for i in range(k1, k2+1):
    out_k1_k2 += str(P_n(i)) + " + "
    sum_k1_k2 += P_n(i)

out_k1_k2 = out_k1_k2[:-2]


S = f"""\
Дана вероятность {p} появления события А в серии из {n} независимых
испытаний. Найти вероятность того, что в этих испытаниях событие А
появится:
а) ровно {k} раз;
б) не менее {k} раз;
в) не менее {k1} раз и не более {k2} раз.

Решение
p = {p}; q = {q}; n = {7}
P_(n) (k) = C_(n)^(k) * p^(k) * q^(n-k), k = 1..n - формула Бернули
(вероятность P_n(k) того, что данное событие наступит ровно k раз в n независимых испытаниях)

а) P_({n}) ({k}) = C_({n})^({k}) * {p}^({k}) * {q}^({n-k}) = {math.comb(n, k)} * {p**k} * {q**(n-k)} = 
{math.comb(n, k) * p**k * q**(n-k)}

б) 
!СЛУЧАЙ, КОГДА k < n/2! ({k} < {n//2} - {k < n/2})
Посчитаем вероятности попадания ровно 1, ... , k-1 раз.
∑_(i=0)^({k-1}) (P_({n}) (i)) = P_({n}) (0) + ... + P_({n}) ({k-1}) = 
= {out_1_k_1} = {sum_1_k_1}

Вероятность того, что шар выпадет не более {k-1} раз равна {sum_1_k_1}
Вероятность того, что шар выпадет не менее {k} раз равна: 1 - ∑_(i=0)^({k-1}) (P_({n}) (i)) = {1-sum_1_k_1} - ответ

!СЛУЧАЙ, КОГДА k > n/2! ({k} > {n//2} - {k > n/2})
Посчитаем вероятности попадания ровно k, ... , n ({k}, ..., {n}) раз.
∑_(i={k})^({n}) (P_({n}) (i)) = P_({n}) ({k}) + ... + P_({n}) ({n}) = {out_k_n} = {sum_k_n}

Вероятность того, что шар выпадет не менее {k} раз равна: ∑_(i={k})^({n}) (P_({n}) (i)) = {sum_k_n} - ответ

в)
∑_(i={k1})^({k2}) (P_({n}) (i)) = P_({n}) ({k1}) + ... + P_({n}) ({k2}) = {out_k1_k2} = {sum_k1_k2}

Ответ:
а) {f(n, k)}
б) {sum_k_n}
в) {sum_k1_k2}

y_(x)- y ̅ =r_(xy)*σ_(by)/σ_(bx) *(x-x̅)  ⇒y_x=r_(xy)⋅σ_(by)/σ_(bx) ⋅x+(y̅ - x ̅x⋅r_(xy)⋅σ_(by)/σ_(bx) )

"""

print(S)