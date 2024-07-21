from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class LoginComponent:

    @staticmethod
    def Login(p_user, p_password):
        try:
            result = False
            data = None
            message = None
            
            # Consulta para verificar si el usuario existe y está activo
            sql_check_user = """
                SELECT COUNT(*) as valor 
                FROM Usuarios 
                WHERE usuario = %s 
                AND contrasena = %s 
                AND estado = TRUE
            """
            
            # Consulta para obtener los detalles del usuario y otros datos necesarios
            sql_user_details = """
                SELECT id_usuario, usuario, nombres, apellidos, correo_electronico, rol, universidad, ultima_hora_acceso
                FROM Usuarios
                WHERE usuario = %s 
                AND contrasena = %s 
                AND estado = TRUE
            """

            record = (p_user, p_password)
            resul_login = DataBaseHandle.getRecords(sql_check_user, 1, record)
            result_user = DataBaseHandle.getRecords(sql_user_details, 1, record)

            if resul_login['result']:
                if resul_login['data']['valor'] > 0:
                    result = True
                    message = 'Login Exitoso'
                    data = result_user['data']
                else:
                    message = 'Login No Válido'
            else:
                message = resul_login['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
