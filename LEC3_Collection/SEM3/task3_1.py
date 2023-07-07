""" 
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа. """
import pprint

tup = ((5, 6), 'check', -18.5 , True, 11, \
       {1, 2}, [1, 2], 2.0 + 2j, b'\x01\x01\x01', {1 : 'one', 2 : 'two'}, 0.5, False)

di = {}

for item in tup:
    if type(item) not in di:
        di[type(item)] = []
    
    di[type(item)].append(item)

print(di)
