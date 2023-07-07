""" ✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка """

def index_sum(lst , start, finish):
    if finish < start:
        start, finish = finish , start
    sum_num = sum(lst[start: finish + 1])
    return sum_num


lst = [12, 35, 25, 14, 86, 10, 8 ,5]
ind_s, ind_f = 3, 6 

print(index_sum(lst, ind_s, ind_f))