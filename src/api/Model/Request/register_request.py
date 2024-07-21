from marshmallow import Schema, fields


class RegisterRequest(Schema):
    user_login_id = fields.String(required=True)
    user_mail = fields.String(required=True)
    user_names = fields.String(required=True)
    user_lastnames = fields.String(required=True)
    user_password = fields.String(required=True)
    