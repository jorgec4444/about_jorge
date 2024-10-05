@echo off
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
if exist public (
    rmdir /s /q public
)
powershell -Command "Expand-Archive -Path frontend.zip -DestinationPath public"
del frontend.zip
deactivate
pause