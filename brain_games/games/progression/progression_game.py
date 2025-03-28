
from random import randint, randrange

LENGTH_OF_NUMBERS = 10
DESCRIPTION = 'What number is missing in the progression?'


def get_random_number():
    return randint(1, 10)


def generate_number_and_true_answer():
    start = get_random_number()
    step = get_random_number()
    random_number = randrange(start, LENGTH_OF_NUMBERS * step, step)
    end = start + (LENGTH_OF_NUMBERS * step)
    list_of_numbers = ''
    
    for i in range(start, end, step):
        if i == random_number:
            list_of_numbers += '..' + ' '
            true_answer = i
        else:
            list_of_numbers += str(i) + ' '
    return list_of_numbers.strip(), str(true_answer)   

