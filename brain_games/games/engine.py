import prompt

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
        print(f"Let's try again, {name}")
        exit()


def congratulation(count_of_correct_answers):
    if count_of_correct_answers == count_of_rounds:
        print(f'Congratulations, {name}!')
        exit()