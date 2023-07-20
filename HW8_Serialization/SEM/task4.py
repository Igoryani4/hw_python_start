""" Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции. """

import csv
import json


def from_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', newline='') as f:
        csv_file = csv.reader(f)
        lst = []
        for i, (k, id_, name) in enumerate(csv_file):
            if i :
                lst.append({'acces': k, 
                            'Id': id_.zfill(10), 
                            'name': name,
                            'hash': hash(id_ + name)
                            })
    with open (json_file, 'w', encoding='utf-8') as f2:
        json.dump(lst, f2, indent=4)


from_csv_to_json('HW8_Serialization/SEM/new_names_level.csv', 'HW8_Serialization/SEM/new_names_level.json')
