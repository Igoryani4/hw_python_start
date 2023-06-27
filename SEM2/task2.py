

data = [10, 15.57, 'Yes', '45', True, '45', 1.0 + 0J, b'\x00\x00\x00']

for i, item in enumerate(data, start=1):
    print(f'№ = {i}; value = {item}; ID = {id(item)}, size = {sys.getsizeof(item)}; Hash = {hash(item)}')
    print(f'is integer : True'if isinstance (item, int) else '____' )
    
