.PHONY: init start run

init:
	mkdir django
	virtualenv --python=python3.4 django/myenv

init2:
	pip install django
	django-admin startproject bookshop ./django
	sed 's/UTC/Europe\/Paris/' django/bookshop/settings.py > django/bookshop/settings.py
	echo -ne "\nSTATIC_ROOT = os.path.join(BASE_DIR, 'static')\n" >> django/bookshop/settings.py

start:
	#source django/myenv/bin/activate
	. django/myenv/bin/activate

run:
	python manage.py runserver
