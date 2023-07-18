""" ● Дополнительные параметры dump и dumps
Функции для сериализации объектов в JSON поддерживают несколько
дополнительных параметров. Они позволяют сделать полученные объекты более
удобочитаемыми для пользователя. Разберём на примере функции dumps. Но стоит
помнить, что функция dump обладает такими же параметрами с тем же смыслом. """


import json
my_dict = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@corp.mail.ru",
    "address": {
        "street": "Central",
        "city": "Metropolis",
        "zipcode": "123456"
    },
    "phone": "+7-999-123-45-67"
}
res = json.dumps(my_dict, indent=2, separators=(',', ':'),
sort_keys=True)
print(res)


import json
a = 'Hello world!'
b = {key: value for key, value in enumerate(a)}
c = json.dumps(b, indent=3, separators=('; ', '= '))
print(c)