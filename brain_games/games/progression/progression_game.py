
from random import randint, randrange

import brain_games.games.engine

length_of_numbers = 10


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


def progression_game():
    brain_games.games.engine.welcome_user()
    print('What number is missing in the progression ?')
    count_of_correct_answers = 0
    for i in range(brain_games.games.engine.count_of_rounds):
        number, true_answer = generate_number_and_true_answer()
        brain_games.games.engine.print_question(number)
        answer = brain_games.games.engine.get_answer()
        brain_games.games.engine.comparison(answer, true_answer)
        count_of_correct_answers += 1
        brain_games.games.engine.congratulation(count_of_correct_answers)
