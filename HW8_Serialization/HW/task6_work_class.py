""" Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
Для тестированию возьмите pickle версию файла из предыдущей задачи. 
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла. """

import pickle
import csv

def picle_to_csv(file_picle, file_csv):
    with (open (file_picle, 'rb')as f1,
          open (file_csv, 'w', encoding='utf-8')as f2):
        picle_reader = pickle.load(f1)
        # print(picle_reader)
        csv_write = csv.writer(f2, dialect='excel-tab', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerows(picle_reader)
        # print(f'{csv_write = }')
# data = b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'

picle_to_csv('HW8_Serialization/SEM/names_level.pickle', 'HW8_Serialization/HW/new_names_tab' )