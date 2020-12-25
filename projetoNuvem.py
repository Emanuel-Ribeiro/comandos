import sys
import os
from github import Github

nomePasta = str(sys.argv[1])

diretorio = os.environ.get('mp')         # adiciona o diretorio dos projetos das variaveis de ambiente
token = os.environ.get('gt')             # adiciona o token do github das variaveis de ambiente

_dir = diretorio + '/' + nomePasta

g = Github(token)

usuario = g.get_user()
login = usuario.login

repo = usuario.create_repo(nomePasta)

comandos = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{nomePasta}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

if sys.argv[2] == "n": 
    os.mkdir(_dir)
    os.chdir(_dir)

    for c in comandos:
        os.system(c)

    print(f'Projeto {nomePasta} criado localmente e no github!')
    os.system('code .')

else:
    print("projeto <nome-Pasta> n")
