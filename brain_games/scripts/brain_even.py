from brain_games.cli import welcome_user
from brain_games.games.game_even import is_even


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    is_even(name)


if __name__ == '__main__':
    main()
