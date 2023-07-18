import csv
with open('HW8_Serialization/LEC/csv/biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, delimiter=' ', dialect='excel-tab',quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
    print(type(line))


    """ ➢ dialect='excel-tab' — указали диалект с табуляцией в качестве разделителя
➢ quoting=csv.QUOTE_NONNUMERIC — передали встроенную константу,
указывающую функции, что числа без кавычек необходимо преобразовать к
типу float. """