from random import randint

import brain_games.games.engine


def get_random_number():
    return randint(1, 100)


def is_even(number):
    return number % 2 == 0


def get_number_and_true_answer():
    number = get_random_number()
    true_answer = 'yes' if is_even(number) else 'no'
    return number, true_answer


def even_game():
    brain_games.games.engine.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_of_correct_answers = 0
    for i in range(brain_games.games.engine.count_of_rounds):
        number, true_answer = get_number_and_true_answer()
        brain_games.games.engine.print_question(number)
        answer = brain_games.games.engine.get_answer()
        brain_games.games.engine.comparison(answer, true_answer)
        count_of_correct_answers += 1
        brain_games.games.engine.congratulation(count_of_correct_answers)

