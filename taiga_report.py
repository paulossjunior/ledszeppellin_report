from taiga import TaigaAPI

api = TaigaAPI()

api.auth(
    username='paulossjunior',
    password='forceknight2009'
)
projects = api.projects.list()

print (projects)

