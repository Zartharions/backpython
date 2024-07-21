from src.api.Services.login_service import LoginService
from src.api.Services.register_service import RegisterService
from src.api.Services.update_service import UpdateService
from src.api.Services.delete_service import DeleteService
from ..Services.user_service import UserService
from src.api.Services.grupo_service import GrupoService
from src.api.Services.listar_materia_service import ListarMateriaId


def load_routes(api):
    #metodo para el login
    api.add_resource(LoginService, '/forum/login')
    #metodo para listar los usuarios
    api.add_resource(RegisterService, '/forum/register')
    #metodo para actualizar un usuario
    api.add_resource(UpdateService, '/segu/update')
    # Método para eliminar un usuario
    api.add_resource(DeleteService, '/segu/delete_user')
    # Método para ver los usuarios
    api.add_resource(UserService, '/user/list')
    # Método para agregar una materia
    api.add_resource(GrupoService, '/forum/create')
    # Método para obtener una materia por ID
    api.add_resource(ListarMateriaId, '/materia/get')