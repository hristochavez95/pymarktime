import views.login
import templates.employee_menu
import models.employees
from time import sleep
from colorama import Fore


# Envia los datos para realizar la marcación de un empleado.
def create_marktime(dni, marked_by):
    if models.employees.create_marktime(dni, marked_by):
        print(Fore.GREEN + 'Marcación realizada correctamente.' + Fore.WHITE)
        sleep(1.5)
    else:
        print(Fore.RED + 'Ocurrio un error al realizar la marcación. Vuelva '
                         'a intentarlo' + Fore.WHITE)
        sleep(2.5)

    # Redirección al menú de empleados.
    templates.employee_menu.menu(views.login.logged_employee)


# Envia los datos necesarios para registrar a un empleado.
def create_employee(employee_info):
    if models.employees.create_employee(employee_info):
        print(Fore.GREEN + 'Empleado registrado correctamente.' + Fore.WHITE)
        sleep(1.5)
    else:
        print(Fore.RED + 'Ocurrio un error al registrar al empleado. Vuelva a '
                         'intentarlo' + Fore.WHITE)
        sleep(2.5)

    # Redirección al menú de empleados.
    templates.employee_menu.menu(views.login.logged_employee)


# Información del empleado a inhabilitar.
def employee_information(dni):
    return models.employees.employee_information(dni)


# Inhabilitación de un empleado.
def disable_employee(dni_employee_to_disable, dni):
    if models.employees.disable_employee(dni_employee_to_disable, dni):
        print(Fore.GREEN + 'Empleado inhabilitado correctamente.' + Fore.WHITE)
        sleep(1.5)
    else:
        print(Fore.RED + 'No se pudo inhabilitar al empleado.' + Fore.WHITE)
        sleep(2.5)


# Cambio de contraseña de empleado.
def change_pass(dni, new_pass):
    if models.employees.change_pass(dni, new_pass):
        print(Fore.GREEN + 'Contraseña cambiada correctamente.' + Fore.WHITE)
        sleep(1.5)
    else:
        print(Fore.RED + 'Ocurrio un error al cambiar la contraseña.' + Fore.WHITE)
        sleep(2.5)