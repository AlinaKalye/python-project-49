from random import randint, choice
from brain_games.library import ask_question, take_answer
from brain_games.library import THREE_TIMES, wrong_answer


def make_list():
    counter = randint(1, 20)
    step_progression = randint(2, 6)
    length_of_list = randint(5, 10)
    i = 1
    list_ = [str(counter)]
    while i < length_of_list:
        counter += step_progression
        list_.append(str(counter))
        i += 1
    hide_element = choice(list_)
    list_[list_.index(hide_element)] = '..'
    list_ = " ".join(list_)
    return list_, hide_element


def find_progression(name):
    print('What number is missing in the progression?')
    i = 1
    while i <= THREE_TIMES:
        question, hide_element = make_list()
        ask_question(question)
        answer = take_answer()
        if answer == hide_element:
            print('Correct!')
            i += 1
        else:
            wrong_answer(name, answer, hide_element)
            return
    print(f"Congratulations, {name}!")
