from brain_games.cli import welcome_user
from brain_games.games.game_prime import is_prime


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    is_prime(name)


if __name__ == '__main__':
    main()
