from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class UpdateComponent:

    @staticmethod
    def update_user(p_id_usuario, p_usuario, p_universidad, p_contrasena_actual, p_nueva_contrasena=None):
        try:
            result = False
            data = None
            message = None
            
            # Verificar la contraseña actual
            sql_verify_password = """
                SELECT contrasena FROM Usuarios
                WHERE id_usuario = %s AND estado = true
            """
            record_verify = (p_id_usuario,)
            verify_result = DataBaseHandle.ExecuteNonQuery(sql_verify_password, record_verify)
            
            if not verify_result['result']:
                message = 'Error al verificar la contraseña'
                return internal_response(result, data, message)
            
            current_password = verify_result['data'][0]['contrasena']
            if current_password != p_contrasena_actual:
                message = 'La contraseña actual es incorrecta'
                return internal_response(result, data, message)

            # Construir la consulta de actualización dinámica
            sql_update = "UPDATE Usuarios SET "
            updates = []
            params = []

            if p_usuario:
                updates.append("usuario = %s")
                params.append(p_usuario)
            
            if p_universidad:
                updates.append("universidad = %s")
                params.append(p_universidad)
                
            if p_nueva_contrasena:
                updates.append("contrasena = %s")
                params.append(p_nueva_contrasena)
            
            if not updates:
                message = 'No se proporcionaron datos para actualizar'
                return internal_response(result, data, message)

            sql_update += ", ".join(updates)
            sql_update += " WHERE id_usuario = %s AND estado = true"
            params.append(p_id_usuario)
            
            update_result = DataBaseHandle.ExecuteNonQuery(sql_update, tuple(params))

            if update_result['result']:
                result = True
                message = 'Usuario actualizado correctamente'
                data = update_result['data']
            else:
                message = update_result['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = str(err)
        finally:
            return internal_response(result, data, message)
