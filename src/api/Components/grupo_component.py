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

            # Insertar el grupo y obtener el id_grupo
            sql_insert_grupo = """
                INSERT INTO Projectg2.Grupos (nombre_grupo, descripcion, id_usuario)
                VALUES (%s, %s, %s) RETURNING id_grupo
            """
            record_grupo = (nombre_grupo, descripcion, id_usuario)
            insert_result_grupo = DataBaseHandle.ExecuteNonQuery(sql_insert_grupo, record_grupo)

            # Debugging output
            print("insert_result_grupo:", insert_result_grupo)

            if insert_result_grupo['result']:
                id_grupo = insert_result_grupo['data']
                if id_grupo:
                    result = True
                    message = 'Grupo creado correctamente'
                    data = id_grupo

                    # Insertar el usuario en el grupo recién creado
                    sql_insert_usuario_grupo = """
                        INSERT INTO Projectg2.Usuarios_Grupos (id_usuario, id_grupo)
                        VALUES (%s, %s)
                    """
                    record_usuario_grupo = (id_usuario, id_grupo)
                    insert_usuario_result = DataBaseHandle.ExecuteNonQuery(sql_insert_usuario_grupo, record_usuario_grupo)

                    # Verificación y manejo de resultado de inserción del usuario
                    if insert_usuario_result['result']:
                        message += ' y usuario agregado al grupo correctamente'
                    else:
                        message = f'Error al agregar usuario al grupo: {insert_usuario_result["message"]}'
                else:
                    message = "No se pudo recuperar el id del grupo creado correctamente"
            else:
                message = insert_result_grupo['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = str(err)
        finally:
            return internal_response(result, data, message)
