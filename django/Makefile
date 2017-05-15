.PHONY: init start run

init:
	virtualenv --python=python3.4 myenv

init2:
	pip install django
	python manage.py makemigrations utilisateurs
	python manage.py migrate utilisateurs
	python manage.py makemigrations livres
	python manage.py migrate livres
	python manage.py makemigrations commandes
	python manage.py migrate commandes

start:
	#source myenv/bin/activate
	#. django/myenv/bin/activate

run:
	python manage.py runserver
