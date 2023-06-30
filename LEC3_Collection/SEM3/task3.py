""" Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях """

data = input('Input spaces value : ')

data_type = ''

if data.isdecimal():
    data_type = 'Целое число'

elif data.replace('.', '').replace('-', '').isdecimal() and data.count('.') == 1 and \
      data.count('-')<=1 and data[-1] != '.' and data[1:].count('-') == 0:
    data_type = 'Отрицательное или Вещественное число'

elif data != data.lower():
    data_type = data.lower()
else:
    data_type = data.upper()

print(f'{data_type = }')



