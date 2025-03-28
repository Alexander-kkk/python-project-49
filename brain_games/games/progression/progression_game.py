
from random import randint, randrange

length_of_numbers = 10
description = 'What number is missing in the progression?'


def get_random_number():
    return randint(1, 10)


def generate_number_and_true_answer():
    start = get_random_number()
    step = get_random_number()
    random_number = randrange(start, length_of_numbers * step, step)
    list_of_numbers = ''
    
    for i in range(start, length_of_numbers * step, step):
        if i == random_number:
            list_of_numbers += '..' + ' '
            true_answer = i
        else:
            list_of_numbers += str(i) + ' '
    return list_of_numbers.strip(), str(true_answer)   

