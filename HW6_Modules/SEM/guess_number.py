
from random import randint


def guess_number(start_, end_ ,tries):
    num = randint(start_, end_,)
    while tries > 0 :
        my_num = int(input('Input youre number : '))
        tries -= 1
        if num > my_num:
            print(f'Highter!, Tries left: {tries}')
        elif num < my_num:
            print(f'Lower!, Tries left: {tries}')
        else:
            return True
    else:
        return False