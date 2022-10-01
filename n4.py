# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Напишите десятичное число: '))
numberb = ''
 
while number > 0:
    numberb = str(number % 2) + numberb
    number = number // 2
 
print(numberb)
