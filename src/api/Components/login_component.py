from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle
#from ..Components.jwt_component import JwtComponent

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
            
            sql_user_groups = """
                SELECT G.nombre_grupo
                FROM Projectg2.Usuarios_Grupos UG
                JOIN Projectg2.Grupos G ON UG.id_grupo = G.id_grupo
                WHERE UG.id_usuario = %s
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

            user_groups = DataBaseHandle.getRecords(sql_user_groups, 1, (user_id,))
            if not user_groups['result']:
                message = user_groups['message']
                return internal_response(result, data, message)

            groups_data = user_groups['data'] if user_groups['data'] is not None else []

            data = {
                **result_user['data'],
                'grupos': [group['nombre_grupo'] for group in groups_data]
            }
            result = True
            message = 'Login Exitoso'
            #data = JwtComponent.TokenGenerate(data)

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
