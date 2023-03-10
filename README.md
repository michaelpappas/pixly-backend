# pixly-backend
Pair Programming with Michael Pappas (@michaelpappas)




# Pixly Backend

# RESTful API Node Express

A RESTful image uploading API using Flask and Postgresql

## Manual Installation

Clone the repo:

```bash
git clone https://github.com/michaelpappas/pixly-backend
cd pixly-backend
```

Set the environment variables:
```bash
touch .env
# open .env and modify the environment variables
```
or
```bash
cp .env.example .env
# open .env and modify the environment variables
```


## Table of Contents

- [Dev Environment](#dev-environment)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)

Development Environment Setup
## dev-environment
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
The frontend will by default look for the backend at 5002 or a specified url in your .env file

## Project Structure

```
\                       # Root folder
 |--app.py              # main routes scripts
 |--image_processing.py # scripts for image processing
 |--models.py           # database models and methods
 |--pixly_aws.py        # scripts for aws
 |--readme.md           # project readme
 |--requirements.txt    # dependencies
```

### API Endpoints

List of available routes:

**Images routes**:\
`GET api/images` - get images (optional filtering)\
`GET api/images/:id` - get image by id\
`POST api/images` - post image\
`PATCH api/images:id` - patch image to increment views\







