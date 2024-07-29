from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle
from ..Components.jwt_component import JwtComponent


class LoginComponent:

    @staticmethod
    def Login(p_user, p_password):
        try:
            result = False
            data = None
            message = None

            sql_check_user = """
                SELECT COUNT(*) as valor 
                FROM Projectg2.Usuarios 
                WHERE usuario = %s 
                AND contrasena = %s 
                AND estado = TRUE
            """

            sql_user_details = """
                SELECT id_usuario, usuario, nombres, apellidos, correo_electronico, rol, universidad, ultima_hora_acceso
                FROM Projectg2.Usuarios
                WHERE usuario = %s 
                AND contrasena = %s 
                AND estado = TRUE
            """

            record = (p_user, p_password)

            resul_login = DataBaseHandle.getRecords(sql_check_user, 1, record)
            if not resul_login['result']:
                message = resul_login['message']
                return internal_response(result, data, message)

            if resul_login['data'] is None or resul_login['data']['valor'] == 0:
                message = 'Login No Válido'
                return internal_response(result, data, message)

            result_user = DataBaseHandle.getRecords(sql_user_details, 1, record)
            if not result_user['result']:
                message = result_user['message']
                return internal_response(result, data, message)

            if result_user['data'] is None:
                message = 'Error al obtener detalles del usuario'
                return internal_response(result, data, message)

            user_id = result_user['data'].get('id_usuario')
            if user_id is None:
                message = 'Error al obtener el ID del usuario'
                return internal_response(result, data, message)


            data = {
                **result_user['data'],

                'token': JwtComponent.TokenGenerate(p_user)

            }
            result = True
            message = 'Login Exitoso'


        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
