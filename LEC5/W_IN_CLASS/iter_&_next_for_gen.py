""" Уже знакомые по сегодняшнему уроку функции iter и next могут работать с
созданными генераторами. Например так: """

from math import factorial


def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

        
my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
""" print(next(my_iter)) """ # StopIteration

def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a 
    for i in range(a, b + 1):
        yield str(i)

for item in gen(10, 1):
    print(f'{item = }')