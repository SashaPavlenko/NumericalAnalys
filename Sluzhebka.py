import pandas as pd

t = pd.read_csv('Форма участника мероприятия (Ответы) - Ответы на форму (1).csv', delimiter=',')
del t['Отметка времени']

print(t)

t.