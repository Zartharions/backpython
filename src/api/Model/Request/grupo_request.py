from marshmallow import Schema, fields

class GrupoRequest(Schema):
    nombre_grupo = fields.String(required=True)
    descripcion = fields.String(required=True)
    id_usuario = fields.Integer(required=True)  # Asegúrate de que esto se incluya en la solicitud
