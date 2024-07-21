from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class RegisterComponent:

    @staticmethod
    def Register(request):
        try:
            result = False
            data = None
            message = None

            # Consulta SQL adaptada a la nueva estructura de la tabla Usuarios
            sql = """
                INSERT INTO Usuarios (usuario, nombres, apellidos, correo_electronico, contrasena, estado, rol, universidad)
                VALUES (%s, %s, %s, %s, %s, TRUE, %s, %s)
            """

            # Campos requeridos por la nueva tabla
            record = (
                request['usuario'], 
                request['nombres'], 
                request['apellidos'], 
                request['correo_electronico'], 
                request['contrasena'], 
                request.get('rol', 'usuario'),  # Valor por defecto 'usuario'
                request.get('universidad', None)  # Valor opcional
            )

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)

            if result_insert['result']:
                result = True
                message = "Registro exitoso"
            else:
                message = result_insert['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
