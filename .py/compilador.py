import PyInstaller.__main__

PyInstaller.__main__.run([
	'--onefile',
	'--clean',
	'-n MaidOS',
	'--add-data="faxina.py:."',
	'--add-data="../README.md:."',
	'--add-data="../LICENSE:."',
	'main.py'
])
