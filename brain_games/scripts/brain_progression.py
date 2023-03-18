from brain_games.cli import welcome_user
from brain_games.games.game_progression import find_progression


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    find_progression(name)


if __name__ == '__main__':
    main()
