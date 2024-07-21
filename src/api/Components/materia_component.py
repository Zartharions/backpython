from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class MateriaComponent:

    @staticmethod
    def add_materia(nombre_materia, descripcion, rama_general, estado, num_creditos):
        try:
            result = False
            data = None
            message = None

            sql_insert = """
                INSERT INTO materias (nombre_materia, descripcion, rama_general, estado, num_creditos)
                VALUES (%s, %s, %s, %s, %s)
            """

            record = (nombre_materia, descripcion, rama_general, estado, num_creditos)

            insert_result = DataBaseHandle.ExecuteNonQuery(sql_insert, record)

            if insert_result['result']:
                result = True
                message = 'Materia agregada correctamente'
                data = insert_result['data']
            else:
                message = insert_result['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
