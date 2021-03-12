import PyInstaller.__main__
from os import remove, getcwd
import shutil


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
    remove(f'{getcwd()[-3]}/ MaidOS.exe')
    shutil.rmtree('build')
    remove(' MaidOS.spec')
    shutil.copy('dist/ MaidOS.exe', f'{getcwd()[:-3]}')
    shutil.rmtree('dist')


compilar()
organizar()
