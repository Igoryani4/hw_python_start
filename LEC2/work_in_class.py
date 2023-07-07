n = input('Введите число: ')
if n.isdigit():
    a = int(n, base=10)
    print(a)
else:
    print(n.isascii())