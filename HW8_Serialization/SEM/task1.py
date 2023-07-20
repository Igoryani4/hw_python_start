""" Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки. """

import ast
import json


def get_json_file():
    with (
        open ('HW8_Serialization/SEM/result.txt', 'r', encoding = 'utf-8')as f1,
        open ('HW8_Serialization/SEM/result.json', 'w', encoding= 'utf-8')as f2
    ):
        my_dict = {}
        for line in f1:
            name, value = line.strip().split('|')
            # my_dict[data[0].upper()] = ast.literal_eval(data[1]) # через AST
            my_dict[name.upper()] = value
        json.dump(my_dict, f2,indent=2)


get_json_file()