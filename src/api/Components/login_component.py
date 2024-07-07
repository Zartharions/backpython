from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from ...utils.database.connection_db import DataBaseHandle

class LoginComponent:

    @staticmethod
    def Login(p_user, p_clave):
        try:
            result = False
            data = None
            message = None
            sql = "SELECT count(*) as valor FROM segu_user WHERE user_login_id = %s AND user_password = %s AND user_state = true"
            sql_user = """
                
                SELECT segu_user.user_id, segu_user.user_login_id, segu_user.user_names, segu_user.user_lastnames, segu_user.user_locked,
                segu_rol.rol_id, segu_rol.rol_name, segu_rol.rol_description,
                segu_module.mod_id, segu_module.mod_name, segu_module.mod_description, segu_module.mod_order, segu_module.mod_icon_name,
                segu_menu.menu_id, segu_menu.menu_name, segu_menu.menu_order, segu_menu.menu_icon_name  
                FROM segu_user
                INNER JOIN segu_user_rol ON segu_user.user_id = segu_user_rol.id_user
                INNER JOIN segu_rol ON segu_user_rol.id_rol = segu_rol.rol_id
                LEFT JOIN segu_menu_rol ON segu_rol.rol_id = segu_menu_rol.mr_rol_id
                LEFT JOIN segu_menu ON segu_menu_rol.mr_menu_id = segu_menu.menu_id
                LEFT JOIN segu_module ON segu_menu.menu_module_id = segu_module.mod_id
                WHERE segu_user.user_login_id = %s AND segu_user.user_password = %s AND segu_user.user_state = true
            """

            record = (p_user, p_clave)
            record_user = (p_user, p_clave)

            resul_login = DataBaseHandle.getRecords(sql,1, record)
            result_user = DataBaseHandle.getRecords(sql_user,1, record_user)

            if resul_login['result']:
                if resul_login['data']['valor'] > 0:
                    result = True
                    message = 'Login Exitoso'
                    data= result_user['data']
                else:
                    message = 'Login No Válido'
            else:
                message = resul_login['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
