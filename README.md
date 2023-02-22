# pixly-backend
Pair Programming with Michael Pappas (@michaelpappas)

Development Environment Setup
=============================

Add a `.env` file in the top level directory and include the following ::
  
  SECRET_KEY=
  DATABASE_URL=postgresql:///pixly
  AWS_ACCESS_KEY_ID=
  AWS_SECRET_ACCESS_KEY=
  AWS_REGION=
  AWS_BUCKET_NAME=
  

You'll need Python3 and PostgreSQL ::

  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt

Create pixly database in psql with CREATE DATABASE pixly;
  
To run the backend run "flask run -p 5002".
The frontend will be default look for the backend at 5002 or a specified url in your .end file

