""" Если после открытия файла в коде возникнет ошибка, строка f.close() не будет
выполнена. В результате ресурсы не освободятся, возможно возникнут проблемы в
работе с открываемым файлом. Чтобы избежать подобных ошибок используют
менеджер контекста with. """

with open('/Users/tochi/Documents/hw_python_start/hw_python_start/HW7/LEC/text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
""" print(f.write('Пока')) # ValueError: I/O operation on closed file. """


with (open('/Users/tochi/Documents/hw_python_start/hw_python_start/HW7/LEC/text_data.txt', 'r+', \
           encoding='utf-8') as f1, \
open('/Users/tochi/Documents/hw_python_start/hw_python_start/bin_data', 'rb') as f2, \
open('/Users/tochi/Documents/hw_python_start/hw_python_start/data.txt', 'r', \
     encoding='utf-8', errors='backslashreplace') as f3):
    print(list(f1))
    print(list(f2))
    print(list(f3))