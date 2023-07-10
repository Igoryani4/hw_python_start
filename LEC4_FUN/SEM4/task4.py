""" ✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии """


def bubble_sort (num_list):
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            if num_list[i] > num_list [j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]

numbers = [1, 12 ,345, 5, -4, 45, 0, 22]

bubble_sort(numbers)
print(numbers)