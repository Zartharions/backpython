from src.utils.general.logs import HandleLogs
from src.utils.general.response import internal_response
from src.utils.database.connection_db import DataBaseHandle
from datetime import datetime

class ListarPComponent:

    @staticmethod
    def listarPublicaciones(id_grupo):
        try:
            result = False
            data = None
            message = None

            # Consulta SQL para obtener las publicaciones del grupo
            sql_query = """
                SELECT id_publicacion, id_usuario, id_grupo, descripcion, likes, visibilidad, reportes, 
                       fecha_hora, hora_publicacion 
                FROM Projectg2.Publicaciones
                WHERE id_grupo = %s
            """

            # Ejecutar la consulta
            resultado = DataBaseHandle.getRecords(sql_query, 0, (id_grupo,))

            if not resultado['result']:
                message = resultado['message']
                return internal_response(result, data, message)

            # Convertir objetos datetime a cadenas de texto
            publicaciones = resultado['data']
            for publicacion in publicaciones:
                if 'fecha_hora' in publicacion:
                    publicacion['fecha_hora'] = publicacion['fecha_hora'].strftime('%Y-%m-%d %H:%M:%S')
                if 'hora_publicacion' in publicacion:
                    publicacion['hora_publicacion'] = publicacion['hora_publicacion'].strftime('%H:%M:%S')

            data = publicaciones
            result = True
            message = 'Publicaciones obtenidas correctamente'

        except Exception as err:
            HandleLogs.write_error(err)
            message = str(err)
        finally:
            return internal_response(result, data, message)
