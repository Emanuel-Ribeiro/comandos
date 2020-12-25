import sys
import os

nomePasta = str(sys.argv[1])

diretorio = os.environ.get('mpw')

_dir = diretorio + '/' + nomePasta

try:
    os.mkdir(_dir)
    os.chdir(_dir)

    os.system('git init')
    os.system(f'echo "# {nomePasta}" > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')

    print(f'projeto {nomePasta} criado localmente!')
    os.system('code .')


except:
    print("projeto <nome_projeto> l")
