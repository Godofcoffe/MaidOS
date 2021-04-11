pyinstaller --noconfirm --log-level=WARN ^
    --onefile  ^
    --add-data="..README;." ^
    --add-data="faxina.py;." ^
    --add-data="form_text.py;." ^
    --icon=..\ ^
