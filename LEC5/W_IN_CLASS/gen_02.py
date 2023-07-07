""" Для создания генераторного выражения используют круглые скобки, внутри
которых прописывается логика выражения. В нашем примере циклический перебор
целых чисел от 97 до 122 и возврат символов из таблицы ASCII с
соответствующими кодами. """

my_gen = (chr(i) for i in range(97, 123))
print(my_gen) # <generator object <genexpr> at0x000001ED58DD7D60>
for char in my_gen:
    print(char)


""" Комбинации for и if в генераторах
и выражениях 

В общем виде генератор можно записать как:"""

""" gen = (expression for expr in sequense1 if condition1
for expr in sequense2 if condition2
for expr in sequense3 if condition3
...
for expr in sequenseN if conditionN) """

""" for expr in sequense1:
    if not condition1:
        continue
for expr in sequense2:
    if not condition2:
        continue
...
for expr in sequenseN:
    if not conditionN:
        continue """