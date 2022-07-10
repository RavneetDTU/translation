# translation
Steps to Setup the project

Install python 3.8

Install MySQL

pip install -r requirements.txt

# Create database:
1. CREATE DATABASE translation;

2. CREATE USER 'translator'@'localhost' IDENTIFIED BY 'translator#123';

3. GRANT ALL PRIVILEGES ON translation.* TO 'translator'@'localhost';

4. alembic upgrade head (this is to create tables and static data)

# Start Project using below command
uvicorn main:app --reload

Access swagger using below url:
http://127.0.0.1:8000/docs
