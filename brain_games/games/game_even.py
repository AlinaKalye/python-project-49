from random import randint
from brain_games.library import ask_question, take_answer
from brain_games.library import THREE_TIMES, wrong_answer


def check_wright_answer(value, wright_value):
    if value == wright_value:
        return 'yes'
    else:
        return 'no'


def is_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    wright_answer = ''
    while i <= THREE_TIMES:
        value = randint(1, 100)
        question = str(value)
        ask_question(question)
        answer = take_answer()
        check_even = value % 2
        wright_answer = check_wright_answer(check_even, 0)
        if answer == wright_answer:
            print('Correct!')
            i += 1
        else:
            wrong_answer(name, answer, wright_answer)
            break
        print(f"Congratulations, {name}!")
