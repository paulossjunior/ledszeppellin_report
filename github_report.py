from github import Github
import csv

g = Github("paulossjunior", "forceknight2009")

usuario = g.get_user()
repositorios = usuario.get_repos()

# Definindo um dicionario que contera os commits desses
autores = {}
repositorio_pesquisa = "X-data"

for repositorio in repositorios:
    #Pegando os repositórios no qual não sou dono
    if repositorio.owner.login != usuario.login and repositorio.name == repositorio_pesquisa:

        print (repositorio.name)

        commits = repositorio.get_commits()

        for commit in commits:

            if (commit.author is not None) and not(commit.author.login in autores):
                autores[commit.author.login] = []
                autores[commit.author.login].append(commit)
            elif (commit.author is not None) and (commit.author.login in autores):
                autores[commit.author.login].append(commit)


#Salvando em arquivo e definindo o dialeto
csv.register_dialect('dialeto', delimiter=',', quoting=csv.QUOTE_NONE)
git_report = open('git_report.csv', 'w')
with git_report:
    git_report_colluns = ['repositorio','autor', 'sha']
    writer = csv.DictWriter(git_report, fieldnames=git_report_colluns)
    writer.writeheader()
    for key, commites in autores.items() :
        for commit in commites:
            writer.writerow({'repositorio': repositorio_pesquisa,'autor' : key, 'sha': commit.sha})
