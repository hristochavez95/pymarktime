from models.connection import connect_to_db
from mysql.connector import errors


# Intenta realizar la marcacioń de un empleado.
# Retorna:
# True o False si la marcación se realizó correctamente.
# Una cadena con un mensaje de error en el caso fallar la operación.
def create_marktime(dni, marked_by):
    # Indica si la marcación se realizó con exito.
    success_marking = True

    # Se intenta una conexión con la BBDD.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'create_marktime'
        parameters = (dni, marked_by)
        cs.callproc(stored_proc, parameters)
        connection.commit()
    except Exception as err:
        success_marking = False
        print(f'Ocurrio un error => {err}')
        connection.rollback()

    cs.close()
    connection.close()

    return success_marking


# Intenta iniciar la sesión de un empleado.
# Retorna:
# Una tupla que contiene la información del usuario en el caso que exista,
# una tupla vacia si la consulta no retorna algun empleado
# None si se enviaron tipos de datos incorrectos al hacer la consulta como por
# ejemplo enviar 7 digitos cuando se ingresa el DNI.
def get_employee(dni, password):
    # Contiene una tupla con los datos del usuario que inició sesión.
    result_set = []

    # Se intenta una conexión con el servidor.
    connection_result = connect_to_db()

    # Conexión con la BBDD.
    connection = connection_result

    try:
        cs = connection.cursor()
        stored_proc = 'get_employee'
        parameters = (dni, password)
        cs.callproc(stored_proc, parameters)

        for row in cs.stored_results():
            result_set = row.fetchall()
    except Exception as err:
        print(f'Ocurrio un error => {err}')

    cs.close()
    connection.close()

    return result_set


# Crear a un empleado.
def create_employee(employee_info):
    # Indica si la marcación se realizó con exito.
    success_create = True

    # Se intenta una conexión con la BBDD.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'create_employee'
        cs.callproc(stored_proc, employee_info)
        connection.commit()
    except Exception as err:
        success_create = False
        print(f'Ocurrio un error => {err}')
        connection.rollback()

    cs.close()
    connection.close()

    return success_create


# Obtiene la información del empleado consultado.
def employee_information(dni):
    result_set = ()

    # Se intenta una conexión con el servidor.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'employee_information'
        parameters = (dni,)
        cs.callproc(stored_proc, parameters)

        for row in cs.stored_results():
            result_set = row.fetchone()
    except Exception as err:
        print(f'Ocurrio un error => {err}')

    cs.close()
    connection.close()

    return result_set


# Inhabilita a un empleado.
def disable_employee(dni_employee_to_disable, dni):
    # Indica si la inhabilitación se realizó con exito.
    success_disabled = True

    # Se intenta una conexión con la BBDD.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'disable_employee'
        parameters = (dni_employee_to_disable, dni)
        cs.callproc(stored_proc, parameters)
        connection.commit()
    except Exception as err:
        success_disabled = False
        print(f'Ocurrio un error => {err}')
        connection.rollback()

    cs.close()
    connection.close()

    return success_disabled


# Habilita a un empleado.
def enable_employee(dni_employee_to_enable, dni):
    # Indica si la inhabilitación se realizó con exito.
    success_enabled = True

    # Se intenta una conexión con la BBDD.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'enable_employee'
        parameters = (dni_employee_to_enable, dni)
        cs.callproc(stored_proc, parameters)
        connection.commit()
    except Exception as err:
        success_enabled = False
        print(f'Ocurrio un error => {err}')
        connection.rollback()

    cs.close()
    connection.close()

    return success_enabled


# Cambia la contraseña de un empleado.
def change_pass(dni, password):
    # Indica si el cambio de contraseña se hizo con exito.
    success_change_pass = True

    # Se intenta una conexión con la BBDD.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'change_pass'
        parameters = (dni, password)
        cs.callproc(stored_proc, parameters)
        connection.commit()
        cs.close()
    except Exception as err:
        success_change_pass = False
        print(f'Ocurrio un error => {err}')
        connection.rollback()
        cs.close()

    connection.close()

    return success_change_pass
