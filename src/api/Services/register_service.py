from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.register_component import RegisterComponent
from src.api.Model.Request.register_request import RegisterRequest
from flask import request
from flask_restful import Resource

class RegisterService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Registro")
            rq_json = request.get_json()
            new_request = RegisterRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = RegisterComponent.Register(rq_json)
            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
