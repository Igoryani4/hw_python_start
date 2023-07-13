def quiz_func(question, vrnt, tries, cor):
    num_opt = ['{}. {}'.format(*u) for u in zip(range(1, len(vrnt) + 1), vrnt)]
    print(f'\n{question}\n', *num_opt, sep='\n', end='\n\n')
    try_num = 0
    while tries > 0:
        choice = int(input('Выберите ответ: '))
        if choice in range(1, len(vrnt) + 1):
            try_num +=1
            if choice == cor:
                return try_num
            else:
                tries -=1
        else:
            print('Wrong input')
    return 0


def get_quiz_dict(correct_opt, tries):
    tasks = ['Два кольца два конца по середине гвоздик', 'Зимой и летом одним цветом', 
             'Висит груша нельзя скушать']
    opt = [['Карандаш', 'Линейка', 'Ножницы'], 
           ['Сосна', 'Ель', 'Береза'], ['Яблоко', 'Ложка', 'Лампочка']]
    quiz_dict = {k: v for k ,v in zip(tasks, opt)}
    for k , c  in zip(quiz_dict, correct_opt):
        tries_count = quiz_func(k, quiz_dict[k], tries , c)
        print(tries_count)

