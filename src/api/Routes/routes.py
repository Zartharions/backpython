from src.api.Services.login_service import LoginService
from src.api.Services.register_service import RegisterService
from src.api.Services.update_service import UpdateService
from ..Services.listar_grupo_service import ListarGService
from src.api.Services.grupo_service import GrupoService
from src.api.Services.listar_todo_service import ListarTGrupos
from src.api.Services.Join_service import JoinService

def load_routes(api):
    # Método para el login
    api.add_resource(LoginService, '/forum/login')
    # Método para registrar usuarios
    api.add_resource(RegisterService, '/forum/register')
    # Método para actualizar un usuario
    api.add_resource(UpdateService, '/forum/update')
    # Método para listar usuarios
    api.add_resource(ListarGService, '/grupo/list')
    # Método para agregar un grupo
    api.add_resource(GrupoService, '/forum/create')
    # Método para obtener una materia por ID
    api.add_resource(ListarTGrupos, '/forum/grupos')

    api.add_resource(JoinService, '/forum/join')

