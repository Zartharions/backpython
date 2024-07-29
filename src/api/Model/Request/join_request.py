from marshmallow import Schema, fields

class JoinRequest(Schema):
    id_usuario = fields.Integer(required=True)
    nombre_grupo = fields.String(required=True)
