from marshmallow import Schema, fields

class UpdateRequest(Schema):
    id_usuario = fields.Integer(required=True)
    usuario = fields.String(required=False)
    universidad = fields.String(required=False)
    contrasena_actual = fields.String(required=True)  # Clave actual obligatoria
    nueva_contrasena = fields.String(required=False)
