""" ● Запись из словаря
Для записи содержимого словаря в CSV используют класс DictWriter. Его параметры
схожи с рассмотренными выше параметрами DictReader. """


import csv
from typing import Iterator


with (
    open('HW8_Serialization/LEC/csv/biostats_tab.csv', 'r', newline='') as f_read,
    open('HW8_Serialization/LEC/csv/biostats_new.csv', 'w', newline='', encoding='utf-8')as f_write):
    csv_read: Iterator[dict] = csv.DictReader(f_read,
                                              fieldnames=["name", "sex", "age", "height", "weight", "office"], 
                                              restval="MainOffice", dialect='excel-tab', 
                                              delimiter=' ',
                                              quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.DictWriter(f_write, 
                               fieldnames=["id", "name","office", "sex", "age", "height", "weight"],
                               dialect='excel-tab',quoting=csv.QUOTE_ALL)
    csv_write.writeheader()
    all_data = []
    for i, dict_row in enumerate(csv_read):
        if i != 0:
            dict_row['id'] = i
            dict_row['age'] += 1
            all_data.append(dict_row)
    csv_write.writerows(all_data)


    import csv
with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.DictWriter(f_write, fieldnames=["number","name", "data"], restval='Hello world!', dialect='excel',
delimiter='#', quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
    csv_write.writeheader()
    dict_row = {}
    for i in range(10):
        dict_row['number'] = i
        dict_row['name'] = str(i)
        csv_write.writerow(dict_row)