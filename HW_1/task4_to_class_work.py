#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

""" for i in range (2):
    for j in range(4):
        if i == 0:
            for k in range(2,6):
                for n in range (2, 11):
                    print( k, ' x ', n, ' = ', k * n)
                print() """

def table ():
    for i in range(2):
        for j in range (2, 11):
            if i == 0:
                 
                for k in range (2, 6):
                    if j == 10 :
                        print (k , ' x ', j, '= ', j * k, end='    ')
                        continue
                    if j * k > 9:
                        print (k , ' x ', j, ' = ', j * k, end='    ')  
                    else:
                        print (k , ' x ', j, ' = ', j * k, end='     ')
            else:
                for k in range (6, 10):
                    if j == 10 :
                        print (k , ' x ', j, '= ', j * k, end='    ')
                        continue
                    if j * k > 9:
                        print (k , ' x ', j, ' = ', j * k, end='    ')  
                    else:
                        print (k , ' x ', j, ' = ', j * k, end='     ')
            print()
        print()

        


print(table())

""" def print_table (a , b):
    print (a, ' x ', b , ' = ', a * b) """
        