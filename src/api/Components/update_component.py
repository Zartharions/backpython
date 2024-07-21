from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class UpdateComponent:

    @staticmethod
    def update_user(p_user_login_id, p_user_names, p_user_mail, p_user_password):
        try:
            result = False
            data = None
            message = None
            
            sql_update = """
                UPDATE segu_user
                SET user_names = %s, user_mail = %s, user_password = %s
                WHERE user_login_id = %s AND user_state = true
            """
            
            record = (p_user_names, p_user_mail, p_user_password, p_user_login_id)

            update_result = DataBaseHandle.ExecuteNonQuery(sql_update, record)

            if update_result['result']:
                result = True
                message = 'Usuario actualizado correctamente'
                data = update_result['data']
            else:
                message = update_result['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
