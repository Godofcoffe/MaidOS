python -m PyInstaller --noconfirm --log-level=WARN ^
--onefile ^
-n MaidOS ^
--add-data="../README.md;." ^
--add-data="faxina.py;." ^
--add-data="form_text.py;." ^
--add-data="../LICENSE;." ^
main.py

@echo off
pause