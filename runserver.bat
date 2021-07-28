@echo off
title runserver
start cmd /k "D: && cd D:\mohammad hossein\python\django\DjangoBlog\venv\Scripts && activate && cd D:\mohammad hossein\python\django\DjangoBlog\mydjangoBlog && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 8000"