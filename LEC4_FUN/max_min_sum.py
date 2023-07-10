""" max (iterable, *[, key , default]) или max(arg1, arg2, *args[, key]) """

lst1 =[]
lst2 = [42, 256, 73]
lst3 = [('Иван', 125_000), ('Николай', 96_000), ('Петр', 109_000)]

print(max(lst1, default='empty')) # когда список пуст 
print(max(*lst2))  # распаковка списка и передача его для вычисления
print(max(lst3, key= lambda x: x[1]))  


# MIN

print(min(lst1, default='None'))
print(min(*lst2))  # распаковка списка и передача его для вычисления
print(min(lst3, key= lambda x: x[1])) 

# SUM

""" sum (iterable, /, start = 0) """

my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))  #начало от значения старт