from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


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

