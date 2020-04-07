"""Módulo validador de inteiros e floats"""


def validadorint(n: int, /):
    try:
        numero = int(n)
        return True
    except Exception as erro:
        print(f'{erro.__class__}')
        return False


def validadorfloat(n: float, /):
    try:
        numero = float(n)
        return True
    except Exception as erro:
        print(f'{erro.__class__}')
        return False
