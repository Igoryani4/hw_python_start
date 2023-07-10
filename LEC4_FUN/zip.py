""" zip(*iterable, strict = False) """

names = ['Иван', 'Николай', 'Петр']
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0,99]

for name, salari, award in zip(names, salaries, awards):
    print(f'{name} заработал {salari:.2f} денег и премию {salari * award :.2f}')