from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.logs import HandleLogs
from src.utils.general.response import internal_response

class JoinComponent:

    @staticmethod
    def grupo_por_nombre(nombre_grupo):
        try:
            sql_query = """
                SELECT id_grupo
                FROM Projectg2.Grupos
                WHERE nombre_grupo = %s
            """
            result = DataBaseHandle.getRecords(sql_query, 1, (nombre_grupo,))

            if result['result'] and result['data']:
                return result['data']['id_grupo']
            else:
                return None

        except Exception as err:
            HandleLogs.write_error(err)
            return None

    @staticmethod
    def usuario_en_grupo(id_usuario, id_grupo):
        try:
            sql_query = """
                SELECT 1
                FROM Projectg2.Usuarios_Grupos
                WHERE id_usuario = %s AND id_grupo = %s
            """
            result = DataBaseHandle.getRecords(sql_query, 1, (id_usuario, id_grupo))

            return result['result'] and result['data'] is not None

        except Exception as err:
            HandleLogs.write_error(err)
            return False

    @staticmethod
    def unir_usuario(id_usuario, nombre_grupo):
        try:
            id_grupo = JoinComponent.grupo_por_nombre(nombre_grupo)
            if not id_grupo:
                return internal_response(False, None, 'Grupo no encontrado')

            if JoinComponent.usuario_en_grupo(id_usuario, id_grupo):
                return internal_response(False, None, 'El usuario ya está en el grupo')

            sql_insert = """
                INSERT INTO Projectg2.Usuarios_Grupos (id_usuario, id_grupo)
                VALUES (%s, %s)
                ON CONFLICT (id_usuario, id_grupo) DO NOTHING
            """

            result = DataBaseHandle.ExecuteNonQuery(sql_insert, (id_usuario, id_grupo))

            if result['result']:
                return internal_response(True, None, 'Usuario unido al grupo exitosamente')
            else:
                return internal_response(False, None, result['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return internal_response(False, None, str(err))
