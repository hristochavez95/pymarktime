import views.actions
import views.login
import views.validations
from templates.banner import banner
from templates.commons import clean_screen
from getpass import getpass

# Permisos que puede tener un empleado:
# 1 -> Puede marcar.
# 2 -> Puede registrar a un empleado.
# 3 -> Puede inhabilitar a un empleado.
# 4 -> Puede habilitar a un empleado.
actions = {
    1: 'Realizar marcación.',
    2: 'Registrar a un empleado.',
    3: 'Inhabilitar a un empleado.',
    4: 'Habilitar a un empleado.',
    5: 'Cambiar contraseña.',
    6: 'Salir del sistema.'
}


# Recoge la información necesaria para crear a un empleado.
def format_new_employee():
    dni = input('Ingrese el DNI del empleado (8 caracteres): ')
    dni = views.validations.dni(dni)

    first_name = input('Ingrese el primer nombre del empleado: ')
    first_name = views.validations.validate_name(first_name, 'primer nombre')

    second_name = input('Ingrese el segundo nombre del empleado: ')
    second_name = views.validations.validate_second_name(second_name, 'segundo nombre')

    last_name = input('Ingrese el primer apellido del empleado: ')
    last_name = views.validations.validate_name(last_name, 'primer apellido')

    second_last_name = input('Ingrese el segundo apellido del empleado: ')
    second_last_name = views.validations.validate_name(second_last_name, 'segundo apellido')

    # Retorna una tupla que contiene los datos del nuevo empleado.
    employee = (dni, first_name, second_name, last_name, second_last_name)
    return employee


# Retorna una lista de acciones que puede realizar un usuario donde cada
# acciónn es una tupla conformada por:
# (número de opción a mostrar, llave de la acción, descripción de la acción).
def get_employee_actions(employee_permissions):
    # Lista de acciones permitidas.
    employee_actions = []

    # Llena la lista de acciones permitidas de acuerdo a los permisos que
    # tiene el usuario.
    order = 1
    for id_action, description in actions.items():
        if id_action in employee_permissions:
            employee_actions.append((order, id_action, description))
            order += 1

    # Agrega la opción para cambiar la contraseña.
    employee_actions.append((order, 5, actions[5]))

    # Agrega una opción para salir del sistema.
    employee_actions.append((order+1, 6, actions[6]))

    return employee_actions


# Ejecuta la acción elegida por el usuario.
# Obtiene la acción a realizar de la lista de acciones que puede realizar
# el usuario.
def execute_action(employee_actions, selected_action, dni=None):
    do = 0

    for action in employee_actions:
        if str(action[0]) == selected_action:
            do = action[1]
            break

    if do == 1:
        views.actions.create_marktime(dni, dni)
    elif do == 2:
        views.actions.create_employee(format_new_employee())
    elif do == 3:
        # Solicita el dni del empleado a inhabilitar.
        employee_to_disable = input('Ingrese el DNI del empleado'
                                    ' (8 caracteres): ')
        employee_to_disable = views.validations.dni(employee_to_disable)

        # Inhabilitación del empleado.
        views.actions.disable_employee(employee_to_disable, dni)
    elif do == 4:
        # Solicita el dni del empleado a habilitar.
        employee_to_enable = input('Ingrese el DNI del empleado (8 caracteres): ')
        employee_to_enable = views.validations.dni(employee_to_enable)

        # Habilitación del empleado.
        views.actions.enable_employee(employee_to_enable, dni)
    elif do == 5:
        # Solicita una nueva contraseña.
        new_pass = getpass('Ingrese su nueva contraseña: ')
        new_pass = views.validations.password(new_pass)

        # Confirmación de la nueva contraseña.
        repeat_pass = getpass('Repita la nueva contraseña: ')
        repeat_pass = views.validations.password(repeat_pass)

        successfull_change = views.validations.equal_password(new_pass, repeat_pass)

        while not successfull_change:
            print("Las contraseñas no coinciden.")
            # Solicita una nueva contraseña.
            new_pass = getpass('Ingrese su nueva contraseña: ')
            new_pass = views.validations.password(new_pass)

            # Confirmación de la nueva contraseña.
            repeat_pass = getpass('Repita la nueva contraseña: ')
            repeat_pass = views.validations.password(repeat_pass)

            successfull_change = views.validations.equal_password(new_pass, repeat_pass)

        views.actions.change_pass(dni, new_pass)
    elif do == 6:
        exit()


# Muestra el meńu principal del empleado.
def menu(employee):
    clean_screen()
    banner()
    dni = employee['dni']
    first_name = employee['first_name'].capitalize()
    last_name = employee['last_name'].capitalize()

    print(f'DNI: {dni}.')
    print(f'Bienvenido(a) {first_name} {last_name}.')
    print('')

    # Muestra los permisos que tiene el usuario.
    print('Usted tiene los siguientes permisos:')
    # employee['permissions'] contiene una tupla con los id de los permisos
    # que tiene el usuario.
    employee_actions = get_employee_actions(employee['permissions'])
    for action in employee_actions:
        print(f'{action[0]}.- {action[2]}')

    # Pregunta al usuario por la acción a realizar.
    print('')
    selected_action = input('Elija el número de acción a realizar: ')
    selected_action = views.validations.selected_action(len(employee_actions), selected_action)

    # Realiza la acción seleccionada por el usuario.
    execute_action(employee_actions, selected_action, employee['dni'])
