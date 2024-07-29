from flask import request
from flask_restful import Resource
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.listar_grupo import ListarGComponent


class ListarGService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio para obtener grupos por usuario")
            rq_args = request.args
            id_usuario = rq_args.get('id_usuario')

            if not id_usuario:
                return response_error("ID de usuario no proporcionado")

            resultado = ListarGComponent.listarGrupo(id_usuario)
            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + str(err))
