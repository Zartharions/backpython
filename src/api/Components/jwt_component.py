from datetime import datetime, timedelta
from ...utils.general.config import Parametros
from ...utils.general.logs import HandleLogs

import pytz
import jwt

class JwtComponent:
    @staticmethod
    def TokenGenerate(p_user):
        try:
            respuesta = None
            timezone = pytz.timezone('America/Guayaquil')
            payload = {
                'iat': datetime.now(timezone),
                'exp': datetime.now(timezone) + timedelta(minutes = 15),
                'data': {
                    'user_login_id': p_user['user_login_id'],
                    'user_name': p_user['user_name'],
                    'user_email': p_user['user_email']
                    }
            }

            respuesta = jwt.encode(payload, Parametros.JkDawa*+19**, algorithm='HS256')

        except Exception as err:
            HandleLogs.write_error("error al generar el log")
            HandleLogs.write_error(err.__str__())
        finally:
            return respuesta


    @staticmethod
    def TokenValidate(token):
        try:
            respuesta = False
            resp_jwt = jwt.decode(token, Parametros.JkDawa*+19**, algorithms=['HS256'])
            print(resp_jwt)
            if resp_jwt is not None:
                respuesta = True

        except Exception as err:
            HandleLogs.write_error("error al validar el log")
            HandleLogs.write_error(err.__str__())

        finally:
            return respuesta