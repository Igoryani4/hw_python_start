""" Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки. """

txt = input('input youre text here: ').split(' ')
start , space = 1 , 1
align = len(max(txt, key = len))
result = {}
txt.sort()

for num, word in enumerate(txt, start):
    print(f'{num} {word:>{align}}')

