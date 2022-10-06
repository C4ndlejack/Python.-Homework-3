# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def pairsProd(size):
    if size < 0:
        print("Задано неверное число!")
    else:
       myList = sample(range(1, 50), size)
       print(f"Ваш список: {myList}")
    prod = 1
    i = 0
    j = 1
    list_length = len(myList)
    print("Произведение пар чисел списка:", end = " ")
    while i < list_length - j:
        prod = myList[i] * myList[list_length - j]
        i += 1
        j += 1
        print(prod, end = " ")
        if i == list_length - j:
            print(myList[i])

pairsProd(int(input("Введите число: ")))