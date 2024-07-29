from src.utils.general.logs import HandleLogs
from src.utils.general.response import internal_response
from src.utils.database.connection_db import DataBaseHandle


class ListarGComponent:

    @staticmethod
    def listarGrupo(id_usuario):
        try:
            result = False
            data = None
            message = None

            # Consulta SQL para obtener el ID y nombre del grupo
            sql_query = """
                SELECT G.id_grupo, G.nombre_grupo
                FROM Projectg2.Usuarios_Grupos UG
                JOIN Projectg2.Grupos G ON UG.id_grupo = G.id_grupo
                WHERE UG.id_usuario = %s
            """

            # Ejecutar la consulta
            resultado = DataBaseHandle.getRecords(sql_query, 0, (id_usuario,))

            if not resultado['result']:
                message = resultado['message']
                return internal_response(result, data, message)

            data = resultado['data']
            result = True
            message = 'Grupos obtenidos correctamente'

        except Exception as err:
            HandleLogs.write_error(err)
            message = str(err)
        finally:
            return internal_response(result, data, message)
