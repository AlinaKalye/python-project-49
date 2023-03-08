from brain_games.cli import welcome_user
from brain_games.games.game_calc import calculate


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    calculate(name)


if __name__ == '__main__':
    main()
