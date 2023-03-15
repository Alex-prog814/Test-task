Quick Start Guide

1. Setting up a virtual environment

   After cloning the project, go to the project folder using the terminal and type the following command:

   ```
   python3 -m venv venv
   ```

   now activate the environment:

   ```
   source venv/bin/activate
   ```

2. Django must be installed, along with all required modules and third-party libraries
   Type the following command:
   ```
   pip3 install -r requirements.txt
   ```
3. Migrations to the database

   Type the command in the terminal:

   ```
   python3 manage.py makemigrations
   ```

   then

   ```
    python3 manage.py migrate
   ```

4. Create superuser

   Enter the following command to create a superuser:

   ```
   python3 manage.py super_user
   ```

   then enter the requested data

5. Before start
   Run test
   ```
   python3 manage.py test applications/user
   ```
6. Server start

   Enter the following command in terminal:

   ```
   python3 manage.py runserver
   ```

   Fine! Project is ready to use.

7. See API docs

   Enter the following in url:

   ```
   http://localhost:8000/api/v1/docs/
   ```
