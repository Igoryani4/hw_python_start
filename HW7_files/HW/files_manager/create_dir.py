

from pathlib import Path
import os


def create_dir(name_dir: str):
    #
    name = Path(Path.cwd() / name_dir)  
    if not name.exists():  # проверка на наличие директория
        name.mkdir()  # создает директорий с именем name_dir в текущем директории
    # os.chdir(name)  # переходим в созданный каталог сделав его текущим

create_dir('HW7_files/HW/test_dir')
