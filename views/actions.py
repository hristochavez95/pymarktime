import time
from colorama import Fore
import views.login as vl
import templates.employee_menu as te
import models.employees as me


# Envia los datos para realizar la marcación de un empleado.
def create_marktime(dni, marked_by):
    if me.create_marktime(dni, marked_by):
        print(Fore.GREEN + 'Marcación realizada correctamente.' + Fore.WHITE)
        time.sleep(1.5)
    else:
        print(Fore.RED + 'Ocurrio un error al realizar la marcación. Vuelva '
                         'a intentarlo' + Fore.WHITE)
        time.sleep(2.5)

    # Redirección al menú de empleados.
    te.menu(vl.logged_employee)


# Envia los datos necesarios para registrar a un empleado.
def create_employee(employee_info):
    if me.create_employee(employee_info):
        print(Fore.GREEN + 'Empleado registrado correctamente.' + Fore.WHITE)
        time.sleep(1.5)
    else:
        print(Fore.RED + 'Ocurrio un error al registrar al empleado. Vuelva a '
                         'intentarlo' + Fore.WHITE)
        time.sleep(2.5)

    # Redirección al menú de empleados.
    te.menu(vl.logged_employee)


# Información del empleado a inhabilitar.
def employee_information(dni):
    return me.employee_information(dni)


# Inhabilitación de un empleado.
def disable_employee(dni_employee_to_disable, dni):
    if me.disable_employee(dni_employee_to_disable, dni):
        print(Fore.GREEN + 'Empleado inhabilitado correctamente.' + Fore.WHITE)
        time.sleep(1.5)
    else:
        print(Fore.RED + 'No se pudo inhabilitar al empleado.' + Fore.WHITE)
        time.sleep(2.5)


# Cambio de contraseña de empleado.
def change_pass(dni, new_pass):
    if me.change_pass(dni, new_pass):
        print(Fore.GREEN + 'Contraseña cambiada correctamente.' + Fore.WHITE)
        time.sleep(1.5)
    else:
        print(Fore.RED + 'Ocurrio un error al cambiar la contraseña.' + Fore.WHITE)
        time.sleep(2.5)