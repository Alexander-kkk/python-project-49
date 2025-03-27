
from random import randint

import brain_games.games.engine


def get_random_number():
    return randint(1, 20)


def generate_number_and_true_answer():
    num1 = get_random_number()
    num2 = get_random_number()
    number = f'{num1} {num2}'
    num_min = min(num1, num2)
    for i in range(num_min, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            true_answer = str(i)
            return number, true_answer
        

def gcd_game():
    brain_games.games.engine.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count_of_correct_answers = 0
    for i in range(brain_games.games.engine.count_of_rounds):
        number, true_answer = generate_number_and_true_answer()
        brain_games.games.engine.print_question(number)
        answer = brain_games.games.engine.get_answer()
        brain_games.games.engine.comparison(answer, true_answer)
        count_of_correct_answers += 1
        brain_games.games.engine.congratulation(count_of_correct_answers)   
