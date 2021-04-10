import PyInstaller.__main__
from subprocess import run


def compilar():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '-n MaidOS.exe',
        '--log-level=WARN',
        '--add-data=faxina.py:.',
	'--upx-dir=/usr/local/share/'
    ])


def organizar():
    run(['rm', '-rf', 'build'], shell=True)
    run(['rm', '-rf', ' MaidOS.spec'], shell=True)
    run(['cp', 'dist/ MaidOS.exe', '..'], shell=True)
    run(['rm', 'rf', 'dist'], shell=True)


compilar()
organizar()
