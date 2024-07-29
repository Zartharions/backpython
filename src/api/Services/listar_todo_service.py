from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_not_found
from src.api.Components.listar_todo_component import GrupoTComponent
from flask_restful import Resource

class ListarTGrupos(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio para obtener todos los grupos")

            resultado = GrupoTComponent.listar_grupos()

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_not_found(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + str(err))
