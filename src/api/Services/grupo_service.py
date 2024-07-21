from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.grupo_component import GrupoComponent
from src.api.Model.Request.grupo_request import GrupoRequest
from flask import request
from flask_restful import Resource

class GrupoService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio para crear grupo")
            rq_json = request.get_json()
            new_request = GrupoRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            # Obtener ID del usuario desde los datos enviados en la solicitud
            id_usuario = rq_json.get('id_usuario')  # Asegúrate de enviar esto desde el front-end

            if not id_usuario:
                return response_error("ID de usuario no proporcionado")

            resultado = GrupoComponent.crear_grupo(
                rq_json['nombre_grupo'],
                rq_json.get('descripcion', ''),
                id_usuario
            )

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
