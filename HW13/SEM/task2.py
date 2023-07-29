'''
Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений
'''



def get_dict(my_dict, key, value = 'key not found'):
    try:
        return my_dict[key]
    except KeyError:
        return value
    


if __name__ == '__main__':
    my_dict = {'g' : 1, 'j' : 2, 'top': 34}
    print(get_dict(my_dict, 'gg', 30 ))
    print(get_dict(my_dict, 'top', 122 ))