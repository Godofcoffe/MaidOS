import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--clean',
    '-n MaidOS',
    '--log-level=WARN',
    '--add-data="faxina.py:."'
])
