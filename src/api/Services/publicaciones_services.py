from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_not_found
from src.api.Components.publicaciones_component import publicacionesComponent
from src.api.Model.Request.publicaciones_request import publicacionesRequest
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError


class publicacionesServices(Resource):

    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Creación de publicación")
            rq_json = request.get_json()
            publicacion_request_schema = publicacionesRequest()

            try:
                user_data = publicacion_request_schema.load(rq_json)
            except ValidationError as err:
                HandleLogs.write_error("Error al validar el request -> " + str(err.messages))
                return response_error("Error al validar el request -> " + str(err.messages))

            resultado = publicacionesComponent.createPublicacion(
                user_data['publicacion_id_usuario'],
                user_data['publicacion_id_grupo'],
                user_data['publicacion_descripcion']
            )

            if resultado['result']:
                return response_success("Ingreso Exitoso")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
