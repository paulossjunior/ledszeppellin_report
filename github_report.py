from github import Github
import csv

g = Github("user_name", "password")

usuario = g.get_user()
repositorios = usuario.get_repos()

# Definindo um dicionario que contera os commits desses
autores = {}
#repositorio_pesquisa = "X-data"
repositorio_pesquisa = "ledszeppellin_report"

for repositorio in repositorios:
    #Pegando os repositórios no qual não sou dono
    if repositorio.name == repositorio_pesquisa:

        commits = repositorio.get_commits()

        for commit in commits:

            if (commit.author is not None) and not(commit.author.login in autores):
                autores[commit.author.login] = []
                autores[commit.author.login].append(commit)
                print ("Login: "+commit.author.login)
                print ("Message: "+commit.commit.message)
                print ("Url: "+commit.commit.url)
                print (commit.commit.author.date)
                print ("Email Committer: "+commit.commit.committer.email)
                print (commit.commit.committer.date)

            elif (commit.author is not None) and (commit.author.login in autores):
                autores[commit.author.login].append(commit)
                print ("Login: "+commit.author.login)
                print ("Message: "+commit.commit.message)
                print ("Url: "+commit.commit.url)
                print (commit.commit.author.date)
                print ("Email Committer: "+commit.commit.committer.email)
                print (commit.commit.committer.date)

#Salvando em arquivo e definindo o dialeto
csv.register_dialect('dialeto', delimiter=',', quoting=csv.QUOTE_NONE)
git_report = open('git_report.csv', 'w')
with git_report:
    git_report_colluns = ['repositorio',
                        'autor',
                        'sha',
                        'message',
                        'url',
                        'autor_date_commit',
                        'email_committer',
                        'commit_date_commit']
    writer = csv.DictWriter(git_report, fieldnames=git_report_colluns)
    writer.writeheader()
    for key, commites in autores.items() :
        for commit in commites:
            writer.writerow({'repositorio': repositorio_pesquisa,
                             'autor' : key,
                             'sha': commit.sha,
                             'message': commit.commit.message,
                             'url': commit.commit.url,
                             'autor_date_commit': commit.commit.url,
                             'email_committer': commit.commit.url,
                             'commit_date_commit': commit.commit.url,
                             }
                             )
