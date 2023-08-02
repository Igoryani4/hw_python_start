'''
Задание №5
Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – 
список пользователей проекта и админ проекта. Класс имеет следующие методы:
Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
Метод входа в систему – требует указать имя и id пользователя. 
Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта. 
Если в списке его нет, то вызывается исключение доступа. 
Если пользователь присутствует в списке пользователей проекта, то пользователь, 
который входит получает его уровень доступа и становится администратором.
Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, 
чем уровень админа, вызывайте исключение уровня доступа.
* метод удаления пользователя из списка пользователей проекта
* метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
'''
import json
from task3 import User

from Exceptions import AccesErorr, LevelError

class Project:
    

    def __init__(self, project_users = None):
        self.project_users = project_users or []
        self.admin = None
        


    def fill_project_users (cls):
        with open ('HW8_Serialization/SEM/names_level.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
            temp = []
            for key in file:
                for user in file[key].items():
                    temp.append(User(user[1], int(user[0]), int(key)))
            return Project(temp)
        
    
    def enter (self, name, id_):
        user = User(name, id_)
        for proj_user in self.project_users:
            if user == proj_user:
                self.admin = proj_user
                break
        else:
            raise AccesErorr(name, id_)
        

    def add_user(self, name, id_, level):
        if level < self.admin.level:
            raise LevelError
        self.project_users.append(name, id_, level)


    def del_user(self, name, id_, level):
        if level < self.admin.level:
            raise AccesErorr
        try:
            self.project_users.remove(name,id_, level)
        except ValueError:
            print('Пользователя нет в списке')


    def __enter__(self):
        return self
    

    def __exit__(self, exc_type, exc_value, traceback):
        self.file = open('HW13/SEM/users-new.py', 'w', encoding='utf-8')
        json.dump([repr(user) for user in self.project_users], self.file, ensure_ascii=False)
        self.file.close


with Project().fill_project_users() as p:
    print(p.project_users)
    p.enter('Dan', 654)
    print(p.admin)
