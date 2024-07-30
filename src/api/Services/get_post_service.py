from flask import request
from flask_restful import Resource
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.get_posts_component import ListarPComponent

class ListarPublicacionesService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio para obtener publicaciones por grupo")
            rq_args = request.args
            id_grupo = rq_args.get('id_grupo')

            if not id_grupo:
                return response_error("ID de grupo no proporcionado")

            resultado = ListarPComponent.listarPublicaciones(id_grupo)
            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + str(err))
