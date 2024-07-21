from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_not_found
from src.api.Components.listar_materia_component import MateriaComponent
from flask import request
from flask_restful import Resource

class ListarMateriaId(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio para obtener materia por ID")
            materia_id = request.args.get('id')
            
            if not materia_id:
                HandleLogs.write_error("El ID de la materia es requerido")
                return response_error("El ID de la materia es requerido")

            resultado = MateriaComponent.listar_materia(materia_id)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_not_found(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
