import views.validations as vv
from templates.banner import banner
from templates.commons import clean_screen
from views.login import login_employee
from colorama import Fore
import getpass


# Retorna el DNI y la contraseña ingresada por el usuario.
def get_dni_pass():
    dni = input('Ingrese su DNI: ')
    dni = vv.dni(dni)

    password = getpass.getpass('Ingrese su contraseña: ')
    password = vv.password(password)

    return dni, password


# Muestra el menú de inicio de sesión.
def login_screen(fail=False):
    clean_screen()
    banner()

    if fail:
        print(Fore.RED + 'DNI o contraseña incorrecta.' + Fore.WHITE)
        print('')

    # Solicitar DNI y contraseña al usuario.
    dni, password = get_dni_pass()

    # Comunicación con view login.
    login_employee(dni, password)
