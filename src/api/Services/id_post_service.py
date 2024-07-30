from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from src.api.Components.publicaciones_component import publicacionesComponent
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success

class PublicacionesByUserService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de publicaciones por usuario")
            user_id = request.args.get('id_usuario')
            if not user_id:
                return response_error("El parámetro 'id_usuario' es requerido")

            resultado = publicacionesComponent.getPublicacionesByUser(user_id)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
