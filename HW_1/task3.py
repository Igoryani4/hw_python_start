#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
#Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ZERO = 0
COUNT = 10
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
for i in range (ZERO, COUNT):
    total = COUNT - i
    print ('Увас осталось ',str(total), ' попыток')
    n = int(input('Отгадайте загаданное число от 0 до 1000 : '))
    if n != num:
        if n > num:
            print('Ваше Число ', n,' больше загаданного')
        else:
            print('Ваше Число ', n,' меньше загаданного')
    else: 
        print("Вы угадали число это число ", num)
if total == 1:
    print('Вы не угадали у Вас закончились попытки, это число ', num,' попробуйте снова ))')