# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
def binConvert(num: int):
    list = []
    while num > 0:
        list.insert(0, num % 2)
        num //= 2
    list = int(''.join(map(str, list)))
    print(list)
binConvert(int(input()))