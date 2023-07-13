from colorama import Fore, Back, Style
from time import sleep

students = [
    {"name": "Elisa Mavinga", "course": "Curso de Python"},
    {"name": "Deisy Costa", "course": "Curso de Python"},
    {"name": "Vanda Muanha", "course": "Curso de Python"},
    {"name": "Isabel Pascoal", "course": "Curso de Python"},
    {"name": "Domingas Queta", "course": "Curso de Python"},
    {"name": "Geunila Gomes", "course": "Curso de Python"},
    {"name": "Alcina Eurico", "course": "Curso de Python"},
    {"name": "Lauriane Vunge", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
    {"name": "Fernanda Zacarias", "course": "Curso de Python"},
]


def header():
    sleep(1.5)
    print("=" * 60)
    print("CODE ACADEMY:GIRLS".center(60))
    print("=" * 60)
    sleep(2.5)
    print(Style.BRIGHT + Fore.YELLOW + "*" * 60)
    print("Bem-vindas ao Curso de Introdução ao Python".center(60))
    print("*" * 60)
    sleep(2.5)


def presentation(students: list):
    for index, student in enumerate(students):
        print(Style.NORMAL + Fore.GREEN, index + 1, "ª", student.get("name"))
        sleep(1)


header()
presentation(students)
