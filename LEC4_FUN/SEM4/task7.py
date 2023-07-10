""" ✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь. """

def is_profitable(my_dict):
        """ return all(sum(v) >= 0 for v in my_dict.values()) """
        return all(map(lambda x: sum (x) > 0, my_dict.values()))


corporate_balance = {
    'Azimuth': [100, -200, 500, -300, 400],
    'Boutique': [600, -500, 300, -100, 200],
    'Voyage': [400, -300, 600, -200, -400,]
}

print(is_profitable(corporate_balance))