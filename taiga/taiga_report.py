from taiga import TaigaAPI
api = TaigaAPI()

api.auth(
    username='xxxxx',
    password='yyyyy'
)


me = api.me()
# Buscando os projetos que sou membro
projects = api.projects.list(member=me.id)
for project in projects:
    if project.name == 'LaCarte':
        tasks = api.tasks.list(project=project.id)
        milestones = api.milestones.list (project=project.id)
        for milestone in milestones:
            print (milestone.name)
            print (milestone.created_date)
            print (milestone.estimated_start)
            print (milestone.estimated_finish)
            print ('-------------------------------')
