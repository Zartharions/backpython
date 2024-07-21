from marshmallow import Schema, fields

class UpdateRequest(Schema):
    user_login_id = fields.String(required=True)
    user_names = fields.String(required=True)
    user_mail = fields.Email(required=True)
    user_password = fields.String(required=True)
