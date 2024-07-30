from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle


class publicacionesComponent:
    @staticmethod
    def getPublicacionesByUser(id_usuario):
        try:
            result = False
            data = None
            message = None

            sql = """
                        SELECT p.id_publicacion, p.descripcion AS descripcion_publicacion, p.likes, p.visibilidad,   
                               g.nombre_grupo
                        FROM projectg2.publicaciones p
                        JOIN projectg2.grupos g ON p.id_grupo = g.id_grupo
                        JOIN projectg2.usuarios_grupos ug ON g.id_grupo = ug.id_grupo
                        WHERE ug.id_usuario = %s
                        """

            params = (id_usuario,)
            result_publicaciones = DataBaseHandle.getRecords(sql, 0, params)
            if result_publicaciones['result']:
                result = True
                data = result_publicaciones['data']
            else:
                message = 'Error al Obtener datos de publicaciones -> ' + result_publicaciones['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def createPublicacion(id_usuario, id_grupo, descripcion):
        try:
            result = False
            data = None
            message = None

            sql = "INSERT INTO projectg2.publicaciones(id_usuario, id_grupo, descripcion, fecha_hora, hora_publicacion) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIME)"
            params = (id_usuario, id_grupo, descripcion)
            result_createPublicacion = DataBaseHandle.execute(sql, params)

            if result_createPublicacion['result']:
                result = True
                data = result_createPublicacion['data']
            else:
                message = 'Error al ingresar datos de publicaciones -> ' + result_createPublicacion['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
