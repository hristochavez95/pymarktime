import views.login
import templates.employee_menu
import models.employees
from time import sleep
from colorama import Fore


# Envia los datos para realizar la marcación de un empleado.
def create_marktime(dni, marked_by):
    # Indica si la marcación se hizo exitosamente y un código de error de
    # existirlo.
    success_marking, sql_code = models.employees.create_marktime(dni, marked_by)

    if success_marking:
        print(Fore.GREEN + 'Marcación realizada correctamente.' + Fore.WHITE)
    else:
        if sql_code == '45000':
            print(Fore.YELLOW + 'Debe de esperar al menos 30 minutos antes de '
                  'hacer una nueva marcación.' + Fore.WHITE)
        else:
            print(Fore.RED + 'Ocurrio un error al realizar la marcación. ' +
                  'Vuelva a intentarlo' + Fore.WHITE)

    sleep(1.5)
    # Redirección al menú de empleados.
    templates.employee_menu.menu(views.login.logged_employee)


# Envia los datos necesarios para registrar a un empleado.
def create_employee(employee_info):
    if models.employees.create_employee(employee_info):
        print(Fore.GREEN + 'Empleado registrado correctamente.' + Fore.WHITE)
    else:
        print(Fore.RED + 'Ocurrio un error al registrar al empleado. Vuelva a '
                         'intentarlo' + Fore.WHITE)

    sleep(1.5)
    # Redirección al menú de empleados.
    templates.employee_menu.menu(views.login.logged_employee)


# Información del empleado a inhabilitar.
def employee_information(employee_to_disable):
    return models.employees.employee_information(employee_to_disable)


# Inhabilitación de un empleado.
def disable_employee(employee_to_disable, dni):
    result = employee_information(employee_to_disable)
    if result is None:
        print(Fore.RED, end='')
        print(f'El empleado con DNI {employee_to_disable} no existe.')
        print(Fore.WHITE, end='')
    elif result[2] == 0:
        print(Fore.RED, end='')
        print(f'El empleado {result[0]} con DNI {employee_to_disable}'
              ' ya se encuentra inhabilitado.')
        print(Fore.WHITE, end='')
    elif result[2] == 1:
        first_name = result[0].capitalize()
        last_name = result[1].capitalize()
        print(Fore.YELLOW, end='')
        response = input('¿Desea inhabilitar al empleado ' + first_name + ' '
                         + last_name + ' con DNI ' + employee_to_disable + '? '
                         'Escriba S o N: ')
        print(Fore.WHITE, end='')

        response = views.validations.response_disable(response)

        if response == 's' or response == 'S':
            if models.employees.disable_employee(employee_to_disable, dni):
                print(Fore.GREEN + 'Empleado inhabilitado correctamente.' + Fore.WHITE)
            else:
                print(Fore.RED + 'No se pudo inhabilitar al empleado.' + Fore.WHITE)

    sleep(1.5)
    templates.employee_menu.menu(views.login.logged_employee)


# Cambio de contraseña de empleado.
def change_pass(dni, new_pass):
    if models.employees.change_pass(dni, new_pass):
        print(Fore.GREEN + 'Contraseña cambiada correctamente.' + Fore.WHITE)
    else:
        print(Fore.RED + 'Ocurrio un error al cambiar la contraseña.' + Fore.WHITE)

    sleep(1.5)


# Habilitación de un empleado.
def enable_employee(employee_to_enable, dni):
    result = employee_information(employee_to_enable)
    if result is None:
        print(Fore.RED, end='')
        print(f'El empleado con DNI {employee_to_enable} no existe.')
        print(Fore.WHITE, end='')
    elif result[2] == 1:
        print(Fore.RED, end='')
        print(f'El empleado {result[0]} con DNI {employee_to_enable}'
              ' ya se encuentra habilitado.')
        print(Fore.WHITE, end='')
    elif result[2] == 0:
        first_name = result[0].capitalize()
        last_name = result[1].capitalize()
        print(Fore.YELLOW, end='')
        response = input('¿Desea habilitar al empleado ' + first_name + ' '
                         + last_name + ' con DNI ' + employee_to_enable + '? '
                         'Escriba S o N: ')
        print(Fore.WHITE, end='')

        response = views.validations.response_disable(response)

        if response == 's' or response == 'S':
            if models.employees.enable_employee(employee_to_enable, dni):
                print(Fore.GREEN + 'Empleado habilitado correctamente.' + Fore.WHITE)
            else:
                print(Fore.RED + 'No se pudo habilitar al empleado.' + Fore.WHITE)

    sleep(1.5)
    templates.employee_menu.menu(views.login.logged_employee)
