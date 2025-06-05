# Salon-Management-System
This project contains 6 apps : accounts,common,core,service,staff,superadmin

#Step To run this project
1. clone this repo
2. create virtual environment and activate it
3. install require package from requirements.txt using pip install -r requirements.txt
4. create .env file in main directory which contains manage.py and paste the following values \n

NAME=database name

DB_USER=database user name

PASSWORD=database password

HOST=127.0.0.1

PORT=3306

EMAIL_HOST=""

EMAIL_HOST_USER=test@gmail.com

EMAIL_HOST_PASSWORD=email password

DEFAULT_FROM_EMAIL=defaultemail@gmail.com

MY_URL=<url>

where database should be mysql.Create Mysql database and paste the credential in abouve created .env.Your mysql server should be working.

3. Run "python manage.py migrate" 
4. Create Super User "python manage.py createsuperuser "
5. Run python manage.py runserver
