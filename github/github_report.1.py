from github import Github,GitAuthor
import csv

def extraindo_dados_git (username, password, repositorios):

    github_app = Github(username, password)

    repositorios_git = github_app.get_user().get_repos()

    # Definindo um dicionario que contera os commits desses
    repositorios_commites = {}

    for repositorio in repositorios_git:
        #Pegando os repositórios no qual não sou dono
        if repositorio.name in repositorios:
            commits = repositorio.get_commits()
            if not(repositorio.name in repositorios_commites):
                    repositorios_commites[repositorio.name] = []
            
            repositorios_commites[repositorio.name].append(commits)
                
    return repositorios_commites

def criando_arquivo_commit_csv (dados):
    #Salvando em arquivo e definindo o dialeto
    csv.register_dialect('dialeto', delimiter=',', quoting=csv.QUOTE_NONE)
    git_report = open('git_commit_report.csv', 'w')
    with git_report:
        git_report_colluns = ['repositorio',
                            'author',
                            'author_email',
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

        for repositorio, list_commites in dados.items() :
            for committes in list_commites:
                for commit in committes:
                    for file in commit.files:
                        writer.writerow(
                            {'repositorio': repositorio,
                                     'author' : commit.commit.author.name,
                                     'author_email': commit.commit.author.email,
                                     'sha': commit.sha,
                                     'message': commit.commit.message,
                                     'url': commit.commit.url,
                                     'author_date_commit': commit.commit.author.date,
                                     'email_committer': check_value(commit.committer,'email'),
                                     'commit_date_commit': commit.commit.committer.date,
                                     'filename': file.filename,
                                     'additions': file.additions,
                                     'deletions': file.deletions,
                                     'blob_url':file.blob_url
                                 }
                                 )

def check_value(_object,attr_name):
    if _object is not None:
        return getattr(_object, attr_name)
    return ''    

def main():

    print ("Buscando dados no Git")
    repositorios = ['ledszeppellin_report','spring_integration_examples']
    dados = extraindo_dados_git("username", "password", repositorios)
    print ("Salvando os dados em um arquivo")
    criando_arquivo_commit_csv(dados)
    print ("Fim")

if __name__ == "__main__":
    main()
