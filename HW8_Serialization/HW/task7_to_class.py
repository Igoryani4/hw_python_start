""" Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Распечатайте его как pickle строку. """

import pickle


def reader_csv(csv_file_name: str) -> bytes:
    """Читает csv файл, отдает """
    with open(csv_file_name, 'r', encoding='utf-8') as f:
        reader = f.read()
        return pickle.dumps(reader)
    
print(reader_csv('HW8_Serialization/HW/new_names_tab'))
    
