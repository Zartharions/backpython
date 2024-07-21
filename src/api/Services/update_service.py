from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.update_component import UpdateComponent
from src.api.Model.Request.update_request import UpdateRequest
from flask import request
from flask_restful import Resource

class UpdateService(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de actualización de usuario")
            rq_json = request.get_json()
            update_request = UpdateRequest()
            error_en_validacion = update_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = UpdateComponent.update_user(
                rq_json['user_login_id'],
                rq_json['user_names'],
                rq_json['user_mail'],
                rq_json['user_password']
            )

            if resultado['result']:
                return response_success(resultado['message'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
