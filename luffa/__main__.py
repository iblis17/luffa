from bottle import run

from .server import application


def main():
    run(application)


if __name__ == '__main__':
    main()
