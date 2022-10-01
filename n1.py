# Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

import random
lst = []
sum = 0
size = int(input("Введите размер списка: "))

for i in range(size):
     elem = random.randint(0, 100)
     lst.append(elem) 
     if elem%10 != 0:
         sum = sum + elem
     else:
          continue    
    
print("Список: ", lst)
print ("Сумма нечетных элементов списка: ", sum)