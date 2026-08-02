@echo off
cd /d "%~dp0"
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_website
echo.
echo Create an admin user now.
python manage.py createsuperuser
python manage.py runserver
pause
