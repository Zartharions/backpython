from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.login_component import LoginComponent
from src.api.Model.Request.login_request import LoginRequest
from flask import request
from flask_restful import Resource


class LoginService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Login")
            rq_json = request.get_json()

            # Crear una instancia de LoginRequest y validar el request JSON
            new_request = LoginRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            # Obtener los parámetros del request JSON
            p_user = rq_json.get('login_user')
            p_password = rq_json.get('login_password')

            # Verificar que los parámetros están presentes
            if not p_user or not p_password:
                return response_error("Usuario o contraseña no proporcionados")

            # Llamar al método de Login
            resultado = LoginComponent.Login(p_user, p_password)

            # Debugging output
            HandleLogs.write_log(f"Resultado del Login: {resultado}")

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + str(err))
