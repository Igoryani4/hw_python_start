import sys

START_SUM = 0

def check_input(message):
    while True:
        inp = int(input(message))
        if inp % 50 != 0:
            print('Не допустимая сумма, должно быть кратно 50')
        else:
            return inp
        

def increase (bal, op):
    inc = check_input('Введите сумму для пополнения :')
    if op % 3 == 0:
        bal += bal * 0.03
    bal += inc
    op += 1
    if bal > 5000000:
        bal -= bal // 10
    return bal, op

def decrease(bal, op):
    if bal > 5000000:
        bal -= bal // 10
    dec = check_input('Введите сумму снятия')
    percent = dec * 0.015
    if percent < 30:
        percent = 30
    elif percent > 600:
        percent = 600
    dec += percent
    if bal > dec:
        bal -= dec
    else:
        print ('Недостаточно средств')
    if op % 3 == 0:
        bal += bal * 0.03
    op += 1
    return bal, op

def start():
    balance = START_SUM
    operation = 1
    while True:
        select = int(input(f'Баланс {balance} \nОперации со счетом : {operation} \n\nДоступные дейстивия :\n1. Пополнить счет \n2. Снять \n3. Выход\nВыберите действие: '))
        match select:
            case 1:
                balance, operation = increase(balance, operation)
            case 2:
                balance, operation = decrease(balance, operation)
            case 3:
                sys.exit()
            case _:
                print ('Повторите попытку')


start()
