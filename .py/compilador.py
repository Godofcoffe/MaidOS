import PyInstaller.__main__
from subprocess import run


def compilar():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--clean',
        '-n MaidOS',
        '--log-level=WARN',
        '--add-data=faxina.py:.'
    ])


def organizar():
    run(['rm', '-rf', 'build'], shell=True)
    run(['rm', '-rf', ' MaidOS.spec'], shell=True)
    run(['cp', 'dist/ MaidOS.exe', '..'], shell=True)
    run(['rm', 'rf', 'dist'], shell=True)


compilar()
organizar()
