from random import choice, randint

import brain_games.games.engine


def get_random_number():
    return randint(1, 20)


def generate_number_and_true_answer():
    operations = ['+', '-', '*']
    num1 = get_random_number()
    num2 = get_random_number()
    operation = choice(operations)
    if operation == '+':
        true_answer = num1 + num2
    elif operation == '-':
        true_answer = num1 - num2
    elif operation == '*':
        true_answer = num1 * num2
    number = f"{num1} {operation} {num2}"
    return number, str(true_answer)


def calc_game():
    brain_games.games.engine.welcome_user()
    print('What is the result of the expression?')
    count_of_correct_answers = 0
    for i in range(brain_games.games.engine.count_of_rounds):
        number, true_answer = generate_number_and_true_answer()
        brain_games.games.engine.print_question(number)
        answer = brain_games.games.engine.get_answer()
        brain_games.games.engine.comparison(answer, true_answer)  # noqa: E501
        count_of_correct_answers += 1
        brain_games.games.engine.congratulation(count_of_correct_answers)