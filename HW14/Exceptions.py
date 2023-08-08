'''
Задание №3
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
'''

class BasicExeption(Exception):
    pass

class LevelError(BasicExeption):
    def __init__(self, value, value_min):
        self.value = value
        self.value_min = value_min



    def __str__(self):
        return f"Ошибка уровня - {self.value} > минимального уровня {self.value_min}"



class AccesErorr(BasicExeption):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Acess danied - {self.value}"



