from random import randint, uniform


start, end = -1000, 1000

def fill_in_file (file_name, lines_num):
    with open (file_name, 'a', encoding='utf-8') as f:
        for _ in range (lines_num):
            f.write(f'{randint(start, end)} | {uniform(start, end)}\n')

            