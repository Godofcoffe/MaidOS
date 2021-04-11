import PyInstaller.__main__

PyInstaller.__main__.run([
	'--onefile',
	'--clean',
	'-n MaidOS',
	'--add-data=form_text.py:.',
	'--add-data=faxina.py:.',
	'--add-data=../README.md:.',
	'--add-data=../LICENSE:.',
	'main.py'
])
