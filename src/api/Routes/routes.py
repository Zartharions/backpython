from src.api.Services.login_service import LoginService
from src.api.Services.user_service import UserService

def load_routes(api):
    #metodo para el login
    api.add_resource(LoginService, '/segu/login')
    #metodo para listar los usuarios
    api.add_resource(UserService, '/user/list')
