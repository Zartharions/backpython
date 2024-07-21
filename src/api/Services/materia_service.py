from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.materia_component import MateriaComponent
from src.api.Model.Request.materia_request import MateriaRequest
from flask import request
from flask_restful import Resource

class MateriaService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio para agregar materia")
            rq_json = request.get_json()
            new_request = MateriaRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = MateriaComponent.add_materia(
                rq_json['nombre_materia'],
                rq_json.get('descripcion', ''),
                rq_json.get('rama_general', ''),
                rq_json['estado'],
                rq_json['num_creditos']
            )
            
            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
