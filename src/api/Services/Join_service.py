from flask import request
from flask_restful import Resource
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.Join_component import JoinComponent
from src.api.Model.Request.join_request import JoinRequest

class JoinService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio para unir usuario a grupo")
            rq_json = request.get_json()
            new_request = JoinRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            id_usuario = rq_json.get('id_usuario')
            nombre_grupo = rq_json.get('nombre_grupo')

            if not id_usuario or not nombre_grupo:
                return response_error("ID de usuario o nombre de grupo no proporcionado")

            resultado = JoinComponent.unir_usuario(id_usuario, nombre_grupo)

            if resultado['result']:
                return response_success(None)  # No hay datos adicionales a enviar
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + str(err))
