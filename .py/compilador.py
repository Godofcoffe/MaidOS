import PyInstaller.__main__


def compilar():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '-n MaidOS.exe',
        '--log-level=WARN',
        '--add-data=faxina.py:.',
	'--upx-dir=/usr/local/share/'
    ])


compilar()
