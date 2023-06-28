""" Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions. """
from math import gcd
import fractions


def pro_list(a,b):
    res = [a[0] * b[0], a[1] * b[1]]
    print(f'Произведение дробей = ','{}/{}'.format(res[0], res[1]))



def sum_num(a,b):
    if a[1] == b[1]:
        print('{}/{}'.format(a[0]+b[0], a[1]))
    else:
        cd = int(a[1]*b[1]/gcd(a[0], b[0]))
        rn = int(cd/a[1]* a[0]+cd/b[1]*b[0])
        g2 = gcd(rn, cd)
        n = int(rn/g2)
        d = int(cd/g2)
        print(f'Сумма дробей = ','{}/{}'.format(n, d) if n != d else n)


def list_to_int(list) -> list:
    for i in range (len(list)):
        list[i] = int(list[i])
    return list

""" print(u'{}\u2044{}'.format(5, 6)) """
str1 = input('Введите дробь в формате 1/4 : ')
str2 = input('Введите дробь в формате 3/4 : ')
a = str1.split('/')
b = str2.split('/')

list_to_int(a)
list_to_int(b)

sum_num(a,b)
pro_list(a,b)

print('Проверка через Format:')
f_one = fractions.Fraction(a[0], a[1]) 
f_two = fractions.Fraction(b[0], b[1])

print('{} + {} = {}'.format(f_one, f_two, f_one + f_two)) 
print('{} * {} = {}'.format(f_one, f_two, f_one * f_two))



""" print(a,b) """

