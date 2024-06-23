##Simple-Task-management-application

The Task Management Application allows users to create, update, and delete tasks, categorize them by status, and filter by priority and due date. Built with Python, Flask (or Django), and MySQL, it features secure user authentication and a responsive interface for efficient task management and enhanced productivity. Sure! Here's a sample README file for your project:

#Task Management Application

This is a simple task management application built using HTML, CSS, JavaScript, Python Django, and MySQL (XAMPP server). The application allows users to register, log in, and manage their tasks efficiently.

#Table of Contents
1. Features
2. Technologies Used
3. Installation
4. Usage
5. Contributing
6. License
7. Contact

#Features
1. User registration and login functionality
2. Create, read, update, and delete tasks
3. User-friendly interface
4. Responsive design

#Technologies Used
1. Frontend:
  a. HTML
  b. CSS
  c. JavaScript
2. Backend:
  a. Python Django
3. Database:
  a. MySQL (using XAMPP server)

#Installation
1. Prerequisites
2. Python 3.x
3. Django
4. MySQL
5. XAMPP

#Steps
1. Clone the repository:
https://github.com/VidishaBora912/Task-Management.git

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate
# On Windows, use `venv\Scripts\activate`

3.Install the required packages: 
  a. pip install django 
  b. pip install mysqlclient 
  c. pip install django-autoslug

4. Set up the MySQL database:
  a. Start XAMPP and activate MySQL.
  b. Create a new database (e.g., task_db).
  c. Update the DATABASES setting in settings.py with your MySQL credentials.

5. Apply migrations:
  a. python manage.py makemigrations
  b. python manage.py migrate

6. Run the development server:
  a. python manage.py runserver

7.Open your browser and navigate to:
  http://127.0.0.1:8000/
  
Usage
1. Register a new user account.
2. Log in with your credentials.
3. Create, update, or delete tasks as needed.
4. Log out when done.
