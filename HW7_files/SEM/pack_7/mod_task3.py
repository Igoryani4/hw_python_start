def unit_file(file_num, file_names,  new_file):
    with(
        open(new_file, 'w', encoding='utf-8') as u,
        open(file_num, 'r', encoding='utf-8') as f1,
        open(file_names, 'r', encoding='utf-8') as f2
    ):
        lst_prod = [int()]

from typing import TextIO


def read_by_line(file: TextIO):
    test = file.readline()
    if not test:
        file.seek(0)
        test = file.readline()

    return test[:-1]