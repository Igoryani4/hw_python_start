'''
Задание №6
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
'''
import  argparse
from dir_walker import walk_dir


def parse_ars():
    parser = argparse.ArgumentParser(description="My HW parser")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директорию')
    args = parser.parse_args()
    return args.p

def main():
    for place in parse_ars():
        for item in (walk_dir(place)):
            print(repr(item))

if __name__ == '__main__':
    main()
# python3 HW15/task.py -p HW15  - запуск из командной строки
