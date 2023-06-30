""" ✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды. """


nums = [12, 12, 11, 11, 13, 14, 18, 17 ,18]
COUNT = 2


for num in nums:
    if nums.count(num) == COUNT:
        for _ in range (COUNT):
            nums.remove(num)

print(nums)