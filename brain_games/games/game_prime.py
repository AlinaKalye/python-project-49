from random import randint
from brain_games.library import ask_question, take_answer
from brain_games.library import THREE_TIMES, wrong_answer


def check_right_answer(value):
    divider = 2
    while divider < value:
        if value % divider == 0:
            return 'no'
        divider += 1
    return 'yes'


def is_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answer = ''
    for _ in range(THREE_TIMES):
        value = randint(2, 100)
        question = str(value)
        ask_question(question)
        answer = take_answer()
        right_answer = check_right_answer(value)
        if answer == right_answer:
            print('Correct!')
        else:
            wrong_answer(name, answer, right_answer)
            return
    print(f"Congratulations, {name}!")
