""" ✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию. """

""" ✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию. """


# Мое решение

from functools import reduce


n_input = input('Введите текст : ')

def unicodeTranslate(input: str) -> list:
    list =[]
    for i in range (1, len(input)):
        list.append(ord(n_input[i]))
    set1 = sorted_up(list)
    return set1


def sorted_up(list2: list) -> list:
    sort_list = sorted(list2)
    sort_list.reverse()
    usl = []
    for item in sort_list:
        if item not in usl:
            usl.append(item)
    return  usl


print(unicodeTranslate(n_input))


# Хороший код с семенара


def uni(str):
    lst = []
    for i in str:
        lst.append(ord(i))
    return sorted(lst, reverse=True)

print(uni(n_input))


def get (text):
    lst = sorted(reduce(lambda l, x : l if ord(x) in l else l + [ord(x)], text, []), reverse=True )
    return lst

print(get(n_input))