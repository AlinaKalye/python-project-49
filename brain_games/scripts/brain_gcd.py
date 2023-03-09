from brain_games.cli import welcome_user
from brain_games.games.game_gcd import find_greatest_common_divisor


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    find_greatest_common_divisor(name)


if __name__ == '__main__':
    main()
