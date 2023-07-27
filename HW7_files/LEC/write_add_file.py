""" С режимами записи мы уже познакомились.
➢ w — создаём новый пустой файл для записи. Если файл существует,
открываем его для записи и удаляем данные, которые в нём хранились.
➢ x — создаём новый пустой файл для записи. Если файл существует, вызываем
ошибку.
➢ a — открываем существующий файл для записи в конец, добавления данных.
Если файл не существует, создаём новый файл и записываем в него.


● Запись методом write
Метод write принимает на вход строку или набор байт в зависимости от того как вы
открыли файл. После записи метод возвращает количество записанной
информации. """


text = 'Lorem ipsum dolor sit amet, consectetur adipisicingelit.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')


""" Метод не добавляет символ перехода на новую строку. Если произвести несколько
записей, они “склеиваются” в файле. """

text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.',\
        'Consequatur debitis explicabo laboriosam sint suscipittemporibus veniam?', \
            'Accusantiumalis amet fugit iste neque non odit quiasaepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')


""" Если каждая строка должна сохранятся в файле с новой строки, необходимо
самостоятельно добавить символ переноса - \n """

""" Запись методом writelines
Метод writelines принимает в качестве аргумента последовательность и записывает
каждый элемент в файл. Элементы последовательности должны быть строками или
байтами в зависимости от режима записи.

В отличии от write этот метод ничего не возвращает. """


with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))

    """ Для того чтобы каждый элемент списка text сохранялся в файле с новой строки
воспользовались строковым методом join. writelines не добавляет переноса между
элементами последовательности. """

""" ● print в файл
Функция print по умолчанию выводит информацию в поток вывода. Обычно это
консоль. Но можно явно передать файловый объект для печати в файл. Для этого
надо воспользоваться ключевым параметром file. """



with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)


""" В отличии от методов записи в файл, функция print добавляет перенос строки.
Кроме того ничто не мешает явно изменить параметр end функции. """



with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)


""" При работе с файлом можно управлять положением файлового объекта в открытом
файле. Действия напоминают движение курсора в строке стрелками влево и
вправо.
● Метод tell
Метод tell возвращает текущую позицию в файле. """


with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
#print(f.tell()) # ValueError: I/O operation on closed file.

""" ● Метод seek
Метод seek позволяет изменить положение “курсора” в файле.
seek(offset, whence=0), где offset — смещение относительно опорной точки, whence -
способ выбора опороной точки.
● whence = 0 - отсчёт от начала файла
● whence = 1 - отсчёт от текущей позиции в файле
● whence = 2 - отсчёт от конца файла
🔥 Важно! Значения 1 и 2 допустимы только для работы с бинарными
файлами. Исключение seek(0, 2) для перехода в конец текстового файла.
Метод возвращает новую позицию “курсора”. """

last = before = 0

with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))

""" В примере выше мы открыли текстовый файл для одновременного чтения и записи.
Переменные last и before хранят позиции двух последних прочитанных строк.
Дочитав файл в цикле while до конца изменяем позицию “курсора” на начало
последней строки и начинаем запись. Таким образом мы сохранили все строки
файла кроме последней и записали новый текст в конец. """

""" ● Метод truncate
truncate(size=None) — метод изменяет размер файла. Если не передать значение в
параметр size будет удалена часть файла от текущей позиции до конца. Метод
возвращает позицию после изменения файла. """

last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate())

""" Если передать параметр size метод изменяет размер файла до указанного числа
символов или байт от начала файла. """

size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))


#task

start = 10
stop = 100
with open('data.bin', 'bw+') as f:
    for i in range(start, stop + 1):
        f.write(str(i).encode('utf-8'))
        if i % 3 == 0:
            f.seek(-2, 1)
    f.truncate(stop)
    f.seek(0)
    res = f.read(start)
    print(res.decode('utf-8'))