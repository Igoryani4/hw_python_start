""" Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте 
генераторное выражение. """
from quiz import quiz_func
import quiz as q

""" task = 'Зимой и летом одним цветом '
variations = ['Сосна', 'Ель', 'Береза'] """
correct = [3, 2, 3]
total_tries = 2


q.get_quiz_dict(correct, total_tries)
""" print(q.quiz_func(task, variations, total_tries, correct)) """
