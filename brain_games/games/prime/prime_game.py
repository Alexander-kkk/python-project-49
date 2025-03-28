from random import randint

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
count_of_divisors_prime_number = 2


def get_random_number():
    return randint(1, 20)


def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == count_of_divisors_prime_number:
        return True


def generate_number_and_true_answer():
    number = get_random_number()
    true_answer = 'yes' if is_prime(number) else 'no'
    return number, true_answer