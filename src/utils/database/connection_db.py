#Permitir conectarme a una base de datos PostgreSQl
import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor
from ..general.config import Parametros
from ..general.logs import HandleLogs
from ..general.response import internal_response

def conn_db():
    return psycopg2.connect(host=Parametros.db_host,
                            port=int(Parametros.db_port),
                            user=Parametros.db_user,
                            password=Parametros.db_pass,
                            database=Parametros.db_name,
                            cursor_factory=RealDictCursor)


class DataBaseHandle:

    @staticmethod
    def getRecords(query, tamanio, record=()):
        try:
            result = False
            message = None
            data = None

            conn = conn_db()
            cursor = conn.cursor()
            if len(record) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, record)

            if tamanio == 0:
                res = cursor.fetchall()
            elif tamanio == 1:
                res = cursor.fetchone()
            else:
                res = cursor.fetchmany(tamanio)

            data = res
            result = True
        except Exception as ex:
            HandleLogs.write_error(ex)
            message = str(ex)
        finally:
            cursor.close()
            conn.close()
            return internal_response(result, data, message)

    @staticmethod
    def ExecuteNonQuery(query, record):
        try:
            result = False
            message = None
            data = None
            conn = conn_db()
            cursor = conn.cursor()
            if len(record) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, record)

            if query.strip().upper().startswith('INSERT') and 'RETURNING' in query.upper():
                res = cursor.fetchone()
                data = res['id_grupo'] if res and 'id_grupo' in res else None
                conn.commit()
            else:
                conn.commit()
                data = cursor.rowcount  # Número de filas afectadas

            result = True
        except Exception as ex:
            HandleLogs.write_error(ex)
            message = str(ex)
        finally:
            cursor.close()
            conn.close()
            return internal_response(result, data, message)

    @staticmethod
    def execute(query, params):
        try:
            # Establecer conexión a la base de datos
            connection = conn_db()
            cursor = connection.cursor()

            # Ejecutar la consulta
            cursor.execute(query, params)
            connection.commit()

            # Cerrar conexión
            cursor.close()
            connection.close()

            return {"result": True, "data": None}
        except Exception as e:
            return {"result": False, "message": str(e)}

    @staticmethod
    def executeUpdate(sql, params):
        try:
            connection = conn_db()  # Asume que `get_connection` obtiene la conexión a la base de datos
            cursor = connection.cursor()
            cursor.execute(sql, params)
            connection.commit()
            return {'result': True, 'data': cursor.rowcount}
        except Exception as e:
            return {'result': False, 'message': str(e)}
        finally:
            cursor.close()
            connection.close()