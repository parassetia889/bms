#!/bin/sh
python ./book_my_show/manage.py makemigrations ; 
python ./book_my_show/manage.py migrate ; 
python ./book_my_show/manage.py runserver 0.0.0.0:8000