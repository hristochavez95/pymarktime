from getpass import getpass
from re import match
from colorama import Fore


# Validación de DNI.
# DNI: Compuesto de 8 dígitos.
def dni(dni):
    pattern = r'^\d{8}$'
    while not match(pattern, dni):
        print(Fore.RED + 'SOLO PUEDE CONTENER 8 DIGITOS.' + Fore.WHITE)
        dni = input('Ingrese un DNI válido: ')

    return dni


# Validación de contraseña de inicio de sesión.
# Contraseña: Compuesta de 4 dígitos.
def password(password):
    pattern = r'^\d{4}$'
    while not match(pattern, password):
        print(Fore.RED + 'SOLO PUEDE CONTENER 4 DIGITOS.' + Fore.WHITE)
        password = getpass('Ingrese una contraseña válida: ')

    return password


# Validación del nombre y los apellidos.
# Nombre o apellidos: Solo puede contener letras.
def validate_name(name, type):
    pattern = r'^[a-zA-Z]+$'
    while not match(pattern, name):
        print(Fore.RED + 'SOLO PUEDE CONTENER LETRAS.' + Fore.WHITE)
        name = input('Ingrese un ' + type + ': ')

    return name.strip()


# Valida el segundo nombre.
# Segundo nombre: Puede estar vacio o contener solo letras.
def validate_second_name(name, type):
    pattern = r'^[a-zA-Z]*$'
    while not match(pattern, name):
        print(Fore.RED + 'SOLO PUEDE CONTENER LETRAS.' + Fore.WHITE)
        name = input('Ingrese un ' + type + ': ')

    if name == '':
        return None
    else:
        return name.strip()


# Valida la respuesta si se deseea deshabilitar a un empleado.
def response_disable(response):
    while response not in ['S', 's', 'N', 'n']:
        response = input('Escriba S o N para inhabilitar al empleado: ')

    return response


# Validar que la contraseña coincida.
def equal_password(new_pass, repeat_pass):
    return new_pass == repeat_pass


# Validación de acción elegida.
def selected_action(qty_actions, selected_action):
    # Cantidad de acciones permitidas.
    qty_actions = [str(x) for x in range(1, qty_actions + 1)]

    while selected_action not in qty_actions:
        selected_action = input('Elija el número de acción a realizar: ')

    return selected_action