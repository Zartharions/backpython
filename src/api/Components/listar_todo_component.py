from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class GrupoTComponent:

    @staticmethod
    def listar_grupos():
        try:
            result = False
            data = None
            message = None

            sql_select = """
                SELECT nombre_grupo
                FROM Projectg2.Grupos
            """

            select_result = DataBaseHandle.getRecords(sql_select, 0)

            if select_result['result']:
                if select_result['data']:
                    result = True
                    data = [record['nombre_grupo'] for record in select_result['data']]
                    message = 'Grupos encontrados'
                else:
                    message = 'No hay grupos registrados'
            else:
                message = select_result['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
