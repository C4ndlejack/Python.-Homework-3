# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def oddList(size):
    if size < 0:
        print("Задано неверное число!")
    else:
       myList = sample(range(1, 50), size)
       print(f"Ваш список: {myList}")
    sum = 0
    i = 0
    list_length = len(myList)
    while i < list_length:
        sum = sum + myList[i]
        i += 2
    print(f"Сумма элементов списка, стоящих на нечетных позициях равна - {sum}")

oddList(int(input("Введите число: ")))
