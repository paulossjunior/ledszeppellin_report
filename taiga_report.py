from taiga import TaigaAPI

api = TaigaAPI()

api.auth(
    username='user',
    password='psw'
)
#buscando os projetos do usuario
projects = api.projects.list()