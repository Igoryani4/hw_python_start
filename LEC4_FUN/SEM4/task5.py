""" ✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.  """

def get_dict(lst1, lst2, lst3):
    new_list = list(map(lambda x: float(x.replace('%', '')), lst3))
    print(new_list)
    my_dict = {n : s / 100 * (b[: -1]) for n, s, b in zip(lst1, lst2, new_list)}
    return my_dict


lst_name = ['Rob', 'Erich', 'Daniel']
rate = [100_000, 120_000, 130_000]
bonus = ['10.25%', '12.34%', '14.45%']

print(get_dict (lst_name, rate, bonus))

