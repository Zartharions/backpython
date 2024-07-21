from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class DeleteComponent:

    @staticmethod
    def delete_user(p_user_login_id):
        try:
            result = False
            data = None
            message = None

            sql_delete = """
                DELETE FROM segu_user
                WHERE user_login_id = %s AND user_state = true
            """

            record = (p_user_login_id,)

            delete_result = DataBaseHandle.ExecuteNonQuery(sql_delete, record)

            if delete_result['result']:
                result = True
                message = 'Usuario eliminado correctamente'
                data = delete_result['data']
            else:
                message = delete_result['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
