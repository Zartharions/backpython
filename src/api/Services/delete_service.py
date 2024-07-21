from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.delete_component import DeleteComponent
from flask import request
from flask_restful import Resource

class DeleteService(Resource):
    @staticmethod
    def delete():
        try:
            HandleLogs.write_log("Ejecutando servicio de eliminación de usuario")
            rq_json = request.get_json()
            user_login_id = rq_json.get('user_login_id')
            
            if not user_login_id:
                HandleLogs.write_error("user_login_id es requerido")
                return response_error("user_login_id es requerido")

            resultado = DeleteComponent.delete_user(user_login_id)

            if resultado['result']:
                return response_success(resultado['message'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
