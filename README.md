# Blog: Coding Green

The goal of this project was to build a simple blog using Django and Django REST Framework. If you want to run the project on your local machine you'll need to follow the setup instructions below. The blog serves the demonstration of my learning process.
Creating this project helped me to learn how to build a website with Django, made me learn more about the frontend components and gives me opportunity to build backend components like RESTful API endpoints using the Django REST Framework.

# Setup: 

## Prerequisites:

- Python version 3.11

- Virtual environment tool `virtualenv`.

  If you don't have already, make sure to install virtualenv. For the installation of `virtualenv` see:
  
  https://virtualenv.pypa.io/en/latest/installation.html

- Database: PostgreSQL
  If you don't have already, make sure to install PostgreSQL version 15.4:

  https://www.postgresql.org/download/

  With this installation the Postgres GUI pgAdmin will be installed as well, unless you uncheck the box for pgAdmin during the installation process. If you did so, you'll need to install pgAdmin separately:

  https://www.pgadmin.org/
 
  The connector (database adapter) to connect your Django project with the database is already included in the requirements.txt file (see Step 3).
  

## 1. Clone the Repository
  Use the following command:
   
  `git clone https://github.com/sasha-cz/blog-coding-green.git`
  
  Navigate to the project directory:

  `cd 'personal_website - Kopie'`

## 2. Activate the Virtual Environment
   
 The virtual environment is already included in the project ('virtualenv_dj_wd'). Activate the virtual environment.

  On macOS/Linux (bash):

  `source virtualenv_dj_wd/bin/activate`
  
  On windows (bash):

`.\virtualenv_dj_wd\Scripts\activate`

## 3. Installation of Dependencies:
   
  You just need to install the packages from the requirements.txt
  To do this run in your activated environment:

  `pip install -r requirements.txt`

## 4. Database Setup:

  Run migrations to set up the database:

   `python manage.py makemigrations`

   `python manage.py migrate`


## 5. Run the Development Server

  Use the following command:

   `python manage.py runserver`

## 6. View the Website in your Browser

  Open your browser and navigate to the Homepage of the blog, located at `http://127.0.0.1:8000/home/`

# MIT license for MDB Free
The HTML templates and the style.css file within this project may include code snippets and templates provided by https://mdbootstrap.com/ (MDB Free) under the terms of the MIT license:

## Copyright notice

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The software is provided "As is", without warranty of any kind, express or implied, including but not limited To the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall The authors or copyright holders be liable for any claim, damages or other liability, whether in an action of Contract, tort or otherwise, arising from, out of or in connection with the software or the use or other Dealings in the software.



  
