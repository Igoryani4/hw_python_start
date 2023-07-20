""" Python предлагает модуль pickle для сериализации и десериализации своих
структур в поток байт. Преобразования возможны в любом месте и в любое время,
если вы используете Python. Но данные окажутся бесполезными, если вы передаёте
их для обработки другим ЯП.
17
🔥 Крайне важно! Модуль pickle не занимается проверкой потока байт на
безопасность перед распаковкой. Не используйте его с тем набором байт,
безопасность которого не можете гарантировать. """


import pickle
import os


res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res = }')


os.system('echo Hello world!')


""" Допустимые типы данных
для преобразования
Модуль pickle может обработать следующие структуры Python:
● None, True и False;
● int, float, complex;
● str, bytes, bytearrays;
● tuple, list, set, dict если они содержат объекты, обрабатываемые pickle;
● встроенные функции и функции созданные разработчиком и доступные из
верхнего уровня модуля, кроме lambda функций;
● классы доступные из верхнего уровня модуля;
● экземпляры классов, если pickle смог обработать их дандер __dict__ или
результат вызова метода __getstate__().
Список достаточно большой, чтобы позволить сериализовывать большую часть
Python структур. """