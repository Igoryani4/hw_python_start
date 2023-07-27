
from files_manager.create_file import create_file
import os

def gen_files(direct: str, data: dict):
    os.chdir(direct)  # переходим в созданный каталог сделав его текущим

    for key, value in data.items():
        create_file(key, amount_file=value)