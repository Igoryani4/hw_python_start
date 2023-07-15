
import os
from random import choices, randint
import string


def gen_files(ext, min_name_len = 6, max_name_len = 30, count = 42):

    folder_name = 'HW7_files/HW/Files'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name) 
    for i in range (count):
        file_name = ''.join(choices(string.ascii_lowercase, k = randint(min_name_len, max_name_len)))
        with open(f'{folder_name}/{file_name}.{ext}', 'wb' )as f:
            f.write(os.urandom(randint(min_name_len, max_name_len)))

