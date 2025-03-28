from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_random_number():
    return randint(1, 100)


def is_even(number):
    return number % 2 == 0


def generate_number_and_true_answer():
    number = get_random_number()
    true_answer = 'yes' if is_even(number) else 'no'
    return number, true_answer

