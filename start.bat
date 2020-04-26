:: Activate Virtual Enviroment - Windows
@ECHO Step #1 - Generate Python Enviroment ...
@python -m venv venv
@ECHO Step #1 - Done

@ECHO Step #2 - Activating Virtual Environment ...
@CD venv/Scripts
@CALL activate  
@CD ../.. 
@ECHO Step #2 - Done

@ECHO Step #3 - Upgradig PIP ...  
@python -m pip install --upgrade pip 
@ECHO Step #3 - Done

@ECHO Step #4 - Isntalling Requirements ...  
@pip install -r requirements.txt 
@ECHO Step #4 - Done

@ECHO Step #5 - Create Migrations
@python manage.py makemigrations
@python manage.py migrate
@ECHO Step #5 - Done

::  @ECHO Step #6 - Create Super User
::  @python manage.py createsuperuser
::  @ECHO Step #6 - Done
@ECHO ---- All Steps - Done with Success! ----