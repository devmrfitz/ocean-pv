#!bin/env/sh

clear
tput setaf 1; echo "Creating virtual environment"; tput sgr0

python -m venv env
source ./env/bin/activate

pip install -r requirements.txt
tput setaf 1; echo "All dependencies installed"; tput sgr0


tput setaf 1; echo "Setting up secret keys"; tput sgr0
mv .env.example .env
tput setaf 1; echo "Setup done"; tput sgr0
tput setaf 1; echo "Please edit '.env' file to include the correct details"; tput sgr0

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata questions.json

tput setaf 1; echo "Please enter superuser details"; tput sgr0       
tput setaf 1; echo "You can use the credentials below to access the admin page at http://127.0.01:8000/admin/"; tput sgr0       

python manage.py createsuperuser
python manage.py runserver
