import os
import platform
import math

WIDTH = 60


# Calcula el espacio alrededor de una palabra o frase.
def qty_chars(text):
    return math.ceil((WIDTH - len(text))/2) - 1


# Imprime un decorador.
def decorator():
    print('*' * WIDTH)


# Limpiar la pantalla.
def clean_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
