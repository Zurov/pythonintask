#Задача 5. Вариант 19
#Напишите программу, которая бы при запуске случайным образом отображала название одной из восьми планет Солнечной системы.

#Primov G. S.
#28.03.2016
print("Программа выводит на экран одну из восьми планет Солнечной системы")
import random
a = random.choice(['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун'])
print (a)
input("\nНажмите Enter")
