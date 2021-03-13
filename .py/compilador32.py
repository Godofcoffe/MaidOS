import PyInstaller.__main__
from os import remove, getcwd
from shutil import rmtree, copy


def compilar():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--clean',
        '-n MaidOS32',
        '--log-level=WARN',
        '--add-data=faxina.py;.'
    ])


def organizar():
    rmtree('build')
    remove(' MaidOS32.spec')
    copy('dist/ MaidOS32.exe', f'{getcwd()[:-3]}')
    rmtree('dist')

compilar()
organizar()
