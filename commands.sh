# Creating a New Project
django-admin startproject projectname

#Add an app to the project
python manage.py startapp appname

# starting the server

python manage.py runserver

# creating Migrations
python manage.py makemigrations

# Migrate the database

python manage.py migrate

# Creating a Super User for the Admin Panel
python manage.py createsuperuser

# Change Any User's Password
python manage.py changepassword username

# Collecting Static Files Into One Folder
python manage.py collectstatic

# admin ps: Guest@987654321