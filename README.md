# Pixly Backend
RESTful Flask/Postgres API for for image processing and uploading to AWS S3

The accompanying frontend repo can be seen [here](https://github.com/michaelpappas/pixly-frontend).

A deployed version can be found [here](https://pappas-pixly.surge.sh).

## Table of Contents
- [Manual Installation](#manual-installation)
- [Dev Environment](#development-environment)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Further Improvements](#further-improvements)

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




## Development Environment

You'll need Python3 and PostgreSQL

```bash
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  # create a virtual environment and install the dependencies
  ```

Create pixly database in psql with
```sql
CREATE DATABASE pixly;
```

To run the backend run "flask run -p 5002".
The frontend will by default look for the backend at 5002 or a specified url in your .env file

### Project Structure

```
\                       # Root folder
 |--.env.example        # example environment variables
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
`PATCH api/images:id` - patch image to increment views

### Further Improvements

- Write Unittest
- Build out tags functionality
- Enable filtering by exif data like manufacturer and device
- Modify image processing to allow for HEIC image upload and exif processing









