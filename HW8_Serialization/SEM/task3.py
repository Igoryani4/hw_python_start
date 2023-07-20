""" Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV. """


import csv
import json

def json_to_csv():
    with(open('HW8_Serialization/SEM/names_level.json', 'r', encoding='utf-8')as j,
         open('HW8_Serialization/SEM/new_names_level.csv', 'w', newline ='', encoding='utf-8')as c
    ):
        json_file = json.load(j)
        dict_list = []
        for k in json_file.keys():
            for i, n in json_file[k].items():
                dict_list.append({'acces': k, 'id_': i, 'name': n})
        writer = csv.DictWriter(c, fieldnames=['acces', 'id_', 'name'])
        writer.writeheader()
        writer.writerows(dict_list)

json_to_csv()