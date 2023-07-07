""" Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
 """


import collections

x = [1, 2, 3, 5, 6, 7, 5, 2]
print(x)
y = collections.Counter(x)
print(y)

print(list(y))



"O (n)"
""" items = collections.defaultdict(list)
for i, item in enumerate(x):
  items[item].append(i)
for item, locs in items.iteritems():
  if len(locs) > 1:
    print ("duplicates of", item, "at", locs) """



"O (n)"
seen = set()
for n in x:
  if n in seen:
    print ("duplicate:", n)
  else:
    seen.add(n)


"O (n ** 2)"
for i in range(len(x)):
  for j in range(i + 1, len(x)):
    if x[i] == x[j]:
      print ("duplicate:", x[i])