from github import Github,GitAuthor
import csv

def extraindo_dados_git (username, password, nome_repositorio):

    github_app = Github(username, password)

    repositorios = github_app.get_user().get_repos()

    # Definindo um dicionario que contera os commits desses
    autores_committes = {}

    for repositorio in repositorios:
        #Pegando os repositórios no qual não sou dono
        if repositorio.name == nome_repositorio:
            commits = repositorio.get_commits()
            for commit in commits:
                if (commit.author is not None) and not(commit.author.login in autores_committes):
                    autores_committes[commit.author.login] = []
                    autores_committes[commit.author.login].append(commit)
                elif (commit.author is not None) and (commit.author.login in autores_committes):
                    autores_committes[commit.author.login].append(commit)

    return autores_committes

def criando_arquivo_commit_csv (dados,nome_repositorio):
    #Salvando em arquivo e definindo o dialeto
    csv.register_dialect('dialeto', delimiter=',', quoting=csv.QUOTE_NONE)
    git_report = open('git_commit_report.csv', 'w')
    with git_report:
        git_report_colluns = ['repositorio',
                            'author',
                            'sha',
                            'message',
                            'url',
                            'author_date_commit',
                            'email_committer',
                            'commit_date_commit',
                            'filename',
                            'additions',
                            'deletions',
                            'blob_url'
                            ]
        writer = csv.DictWriter(git_report, fieldnames=git_report_colluns)
        writer.writeheader()

        for key, commites in dados.items() :
            for commit in commites:
                for file in commit.files:
                    writer.writerow({'repositorio': nome_repositorio,
                                     'author' : key,
                                     'sha': commit.sha,
                                     'message': commit.commit.message,
                                     'url': commit.commit.url,
                                     'author_date_commit': commit.commit.author.date,
                                     'email_committer': commit.committer.email,
                                     'commit_date_commit': commit.commit.committer.date,
                                     'filename': file.filename,
                                     'additions': file.additions,
                                     'deletions': file.deletions,
                                     'blob_url':file.blob_url
                                 }
                                 )
def main():

    print ("Buscando dados no Git")
    dados = extraindo_dados_git("username", "password", "repositorio")
    print ("Salvando os dados em um arquivo")
    criando_arquivo_commit_csv(dados,"repositorio")
    print ("Fim")

if __name__ == "__main__":
    main()
