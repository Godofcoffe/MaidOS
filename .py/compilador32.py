import PyInstaller.__main__
from os import remove, getcwd
from shutil import rmtree, copy


def compilar():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--clean',
        '-n MaidOS86',
        '--log-level=WARN',
        '--add-data=faxina.py;.'
    ])


def organizar():
    rmtree('build')
    remove(' MaidOS86.spec')
    copy('dist/ MaidOS86.exe', f'{getcwd()[:-3]}')
    rmtree('dist')


compilar()
organizar()
