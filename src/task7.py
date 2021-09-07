'''
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
'''


a = int(input())
b = int(input())
while a and b:
    if a > b:
        a = a % b
    else:
        b = b % a
print('НОД =', a + b)
