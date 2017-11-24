from taiga import TaigaAPI

api = TaigaAPI()

api.auth(
    username='XXXXXX',
    password='YYYYYYY'
)
#buscando os projetos do usuario
api2 = TaigaAPI(token=api.token)
projects = api2.projects.list()

