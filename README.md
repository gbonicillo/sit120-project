# Requirements

python 3.8

pip3

virtualenv (for creating a virtual environment for python)

npm

mysql (not needed if using sqlite)

# Setting up

## API

```bash
# FROM PROJECT DIRECTORY

$ cd api/

# install virtualenv
$ pip3 install virtualenv

# create virtualenv named "env" or any name (1st time only)
$ virtualenv myenv

# activate virtualenv
$ source myenv/bin/activate

# install dependencies
$ pip3 install requirements.txt

# when you're done with working with the env
# as in you're done with running the api server etc

$ deactivate myenv
```

## Client

```bash
# FROM PROJECT DIRECTORY

$ cd client/

# install dependencies
$ npm install
```

# Database setup

## SQLite (set as default)

You don't have to do anything

## MySQL

You can use the [official GUI](https://dev.mysql.com/downloads/workbench/) for these or Google how to do these

1) Create a database named `onlineKarenderya`
2) Create a user in mysql and add all permissions for `onlineKarenderya`
3) In `api/api/settings.py` find this entry and put your user's username and password

```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onlineKarenderya',
        'USER': '<your username here>',
        'PASSWORD': '<your password here>',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

## Creating the super user

```bash
# FROM PROJECT DIRECTORY
$ cd api/

# Create database migrations
$ python3 manage.py makemigrations

# Apply migrations
$ python3 manage.py migrate


# Create a superuser (administrator user)
$ python3 manage.py createsuperuser

```

# Running the Project
***BOTH API AND CLIENT SERVERS MUST BE RUNNING***
## API

```bash
# FROM PROJECT DIRECTORY
$ cd api/

# Activate virtualenv
$ source myenv/bin/activate

# Run API server (Ctrl + C to stop server)
$ python3 manage.py runserver

# When you're donw
$ deactivate
```

## Client

```bash
# FROM PROJECT DIRECTORY
$ cd client/

# Run client server
$ npm run dev
```

# Important URLS

* `localhost:8000/admin` - The Admin page, you can login with superuser here
* `localhost:8000/api` - The API

* `localhost:3000` - Homepage of client