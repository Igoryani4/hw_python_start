""" С одним из генераторов мы уже знакомы. Это объект, возвращаемый функцией
range. При создании генератора мы указываем диапазон перебираемых целых
чисел, но не сохраняем их в памяти. Каждое из значений генерируется на
очередном витке цикла. """

a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')


