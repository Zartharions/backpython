from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class MateriaComponent:

    @staticmethod
    def listar_materia(materia_id):
        try:
            result = False
            data = None
            message = None

            sql_select = """
                SELECT id, nombre_materia, descripcion, rama_general, estado, num_creditos
                FROM materias
                WHERE id = %s
            """

            record = (materia_id,)

            select_result = DataBaseHandle.getRecords(sql_select, 1, record)

            if select_result['result']:
                if select_result['data']:
                    result = True
                    data = select_result['data']
                    message = 'Materia encontrada'
                else:
                    message = 'Materia no encontrada'
            else:
                message = select_result['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
