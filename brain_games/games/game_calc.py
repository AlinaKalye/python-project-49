from random import randint
from brain_games.library import ask_question, take_answer
from brain_games.library import THREE_TIMES, wrong_answer


def calculate(name):
    print('What is the result of the expression?')
    i = 1
    value = 0
    # THREE_TIMES = 3
    while i <= THREE_TIMES:
        value1 = randint(1, 10)
        value2 = randint(1, 10)
        operator = randint(1, 3)
        question = ''
        if operator == 1:
            value = value1 + value2
            question = f'{value1} + {value2}'
        if operator == 2:
            value = value1 - value2
            question = f'{value1} - {value2}'
        if operator == 3:
            value = value1 * value2
            question = f'{value1} * {value2}'
        ask_question(question)
        answer = take_answer()
        if answer == str(value):
            print('Correct!')
            i += 1
        else:
            wrong_answer(name, answer, value)
            break
        if i > THREE_TIMES:
            print(f"Congratulations, {name}!")
