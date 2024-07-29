from marshmallow import Schema, fields

class RegisterRequest(Schema):
    usuario = fields.String(required=True)
    nombres = fields.String(required=True)
    apellidos = fields.String(required=True)
    correo_electronico = fields.String(required=True)
    contrasena = fields.String(required=True)
    rol = fields.String()  # Opcional, por defecto 'usuario'
    universidad = fields.String(required=True)  # Opcional
