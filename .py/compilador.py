import PyInstaller.__main__
from shutil import rmtree, copyfile
from os import system, getlogin

raiz = f'C:Users/{getlogin()}/Documents/git/repositorios/MaidOS/'
def compilar():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--clean',
        '-n MaidOS',
        '--log-level=WARN',
        '--add-data=faxina.py;.'
    ])


def organizar():
    #rmtree('build')
    #system('del /F /A " MaidOS.spec"')
    system(f'move "{raiz}.py/dist/MaidOS.exe" "{raiz}"')
    #rmtree('dist')


#compilar()
organizar()
