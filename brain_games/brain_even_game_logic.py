from random import randint

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def display_questions_and_get_answers():
    count = 0
    while True:
        number = get_random_number()
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        true_answer = 'yes' if number % 2 == 0 else 'no'
        if answer.lower() == true_answer:
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{true_answer}'")
            print(f"Let's try again, {name}")
            break


def get_random_number():
    return randint(1, 100)
