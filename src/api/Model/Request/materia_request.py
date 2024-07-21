from marshmallow import Schema, fields

class MateriaRequest(Schema):
    nombre_materia = fields.String(required=True)
    descripcion = fields.String(required=True)
    rama_general = fields.String(required=True)
    estado = fields.Boolean(required=True)
    num_creditos = fields.Integer(required=True)
