from marshmallow import Schema, fields

class publicacionesRequest(Schema):
    publicacion_id_usuario = fields.Integer(required=True)
    publicacion_id_grupo = fields.Integer(required=True)
    publicacion_descripcion = fields.String(required=True)
