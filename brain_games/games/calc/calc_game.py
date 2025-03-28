from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


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