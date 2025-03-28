import prompt

import brain_games.games.calc.calc_game
import brain_games.games.even.even_game
import brain_games.games.gcd.gcd_game
import brain_games.games.progression

count_of_rounds = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def print_question(number): 
    print(f'Question: {number}')


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def comparison(answer, true_answer):
    if answer == true_answer:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(.")
        print(f"Correct answer was '{true_answer}'")
        print(f"Let's try again, {name}!")
        exit()


def congratulation(count_of_correct_answers):
    if count_of_correct_answers == count_of_rounds:
        print(f'Congratulations, {name}!')
        exit()


def play_game(game_module):
    brain_games.games.engine.welcome_user()
    print(game_module.description)
    count_of_correct_answers = 0
    for i in range(count_of_rounds):
        number, true_answer = game_module.generate_number_and_true_answer()
        print_question(number)
        answer = get_answer()
        comparison(answer, true_answer)
        count_of_correct_answers += 1
        congratulation(count_of_correct_answers)
