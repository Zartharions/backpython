from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class GrupoComponent:

    @staticmethod
    def crear_grupo(nombre_grupo, descripcion, id_usuario):
        try:
            result = False
            data = None
            message = None

            sql_insert_grupo = """
                INSERT INTO Grupos (nombre_grupo, descripcion, id_usuario)
                VALUES (%s, %s, %s) RETURNING id_grupo
            """

            record_grupo = (nombre_grupo, descripcion, id_usuario)
            insert_result_grupo = DataBaseHandle.ExecuteNonQuery(sql_insert_grupo, record_grupo)

            if insert_result_grupo['result']:
                id_grupo = insert_result_grupo['data'][0]['id_grupo']
                result = True
                message = 'Grupo creado correctamente'
                data = id_grupo
                # Agregar al usuario al grupo recién creado
                sql_insert_usuario_grupo = """
                    INSERT INTO Usuarios_Grupos (id_usuario, id_grupo)
                    VALUES (%s, %s)
                """
                record_usuario_grupo = (id_usuario, id_grupo)
                DataBaseHandle.ExecuteNonQuery(sql_insert_usuario_grupo, record_usuario_grupo)
            else:
                message = insert_result_grupo['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
