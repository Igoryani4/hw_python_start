""" Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов. """

import json
from pathlib import Path
import pickle


def from_json_pickle(directory):
    files = [f for f in Path(directory).iterdir() if f.suffix == '.json']
    for file in files:
        with(
            open(file, 'r', encoding='utf-8') as f1,
            open(f'HW8_Serialization/SEM/{file.stem}.pickle', 'wb') as f2
        ):
            date = json.load(f1)
            pickle.dump(date, f2)

from_json_pickle('HW8_Serialization/SEM')
print(Path().cwd())

            