

# Функция принимает список чисел
# Отсотрируйте список по убыванию суммы цифр

def sort_list(num):
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    return summ

list1 = [11, 13, 10, 18, 12, 14, 17, 15, 20, 19, 16]

print(sorted(list1, key=sort_list, reverse=True))