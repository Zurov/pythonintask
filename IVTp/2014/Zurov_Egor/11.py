﻿# Задача 5. Вариант 6.

# Напишите программу, которая бы при запуске случайным образом отображала название одного из восьми соборов Московского кремля.

# Зуров Е.А.
# 12.09.2016

import random

print('Программа случайным образом отображает название одного из восьми соборов Московского кремля.\n')
cath = ['Успенский собор', 'Благовещенский собор', 'Архангельский собор', 'Колокольня Ивана Великого', 'Храм Положения ризы Божией Матери во Влахерне', 'Патриарший дворец и собор Двенадцати Апостолов', 'Церковь Рождества Богородицы на Сенях', 'Верхоспасский собор']
a = random.randint(0,7)
print(cath[a]+(' - один из соборов Московского кремля.'))
input('\n\nНажмите Enter для выхода.')
