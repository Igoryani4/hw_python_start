from random import randint, sample
from re import findall
import string



def fill_in_file(file_name, lines_num):
    count = 0
    with open (file_name, 'a', encoding='utf-8') as f:
        while count < lines_num:
            name = ''.join(sample(string.ascii_lowercase, randint(4, 7)))
            if len(findall('[aeiouyAEIOYU]', name)) > 0:
                f.write(f"{''.join(name).capitalize()} \n")
                count +=1
#Не работает\

fill_in_file('name_test.txt', 5)