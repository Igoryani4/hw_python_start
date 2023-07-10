""" ✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно. """

def create_char_dict (st, en):
    return {chr(i): i for i in range (st, en + 1)}

satart , end = sorted(map(int , input('Введите два числа через пробел : ').split()))

print(create_char_dict(satart, end))


def create_dict (txt): # Не работает почему то
    min_num, max_num = min(int(txt.split()), min(int(txt.split())))
    res = {}
    for i in range (min_num , max_num + 1):
        res[chr(i)] = i
    return res

""" text = input('input : ') """
""" print(create_dict(text)) """