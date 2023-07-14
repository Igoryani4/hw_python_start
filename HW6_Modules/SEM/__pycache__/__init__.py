'''
Задача 8
Создайте пакет с всеми модулями, которые вы создали за время занятия.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.
'''

from guess_number import guess_number
from module7 import check_date
from module7 import check_leap_yeare
from quiz import get_quiz_dict

__all__ = ['guess_number', 'check_date', 'check_leap_yeare', 'get_quiz_dict']
