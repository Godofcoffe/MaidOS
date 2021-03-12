import PyInstaller.__main__

PyInstaller.__main__.run([
    'faxina.py',
    '--onefile',
    '--clean',
    '-n Faxina',
    '--log-level=WARN',
])
