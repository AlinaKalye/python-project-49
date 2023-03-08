import prompt


THREE_TIMES = 3


def wrong_answer(name, answer, wright_answer):
    WRONG_TEXT = ' is wrong answer ;(. Correct answer was '
    print(f"'{answer}'{WRONG_TEXT}'{wright_answer}'.")
    print(f"Let's try again, {name}!")


def ask_question(question):
    print('Question: ' + question)


def take_answer():
    answer = prompt.string('Your answer: ')
    return answer
