from random import randint
import math
from brain_games.library import ask_question, take_answer
from brain_games.library import THREE_TIMES, wrong_answer


def find_greatest_common_divisor(name):
    print('Find the greatest common divisor of given numbers.')
    i = 1
    value = 0
    while i <= THREE_TIMES:
        value1 = randint(1, 50)
        value2 = randint(1, 50)
        value = math.gcd(value1, value2)
        question = f'{value1}  {value2}'
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
