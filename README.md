# Mini Parameter Store

Mini Parameter Store is REST API project implemented in Django REST framework. Swagger is added for documentation of API.

------------------------------------------------------------------------
Pre-requisite
-----
- python 3.9
- pip3

```
brew install python 3.9.4
```

**virtualenv** is a tool that is used to create a virtual environment that install all
python packages and python from that environment.

**Installation**

```
pip3 install virtualenv
```

-----------------------------------------------------------------------
Setup
-----

Create .env file using content of .env.example and update credentials where required.

    $ cd parameterstore && touch .env && .env << .env.example

Create and Activate virtual environment

```
cd ..
python3.9 -m venv env
source env/bin/activate
```

Install all required packages in ***requirements.txt***

    $ pip install -r requirements.txt

------------------------------------------------------------------------

Run Server
----------

Migrate database to load schema changes

    $ python manage.py db upgrade

Run flask server

    $ python manage.py runserver

```
Server will be running on http://127.0.0.1:8000/
```
-------------------------------------------------------------------------
To see how you approach software development in an environment like ours, we'd like you to implement a simple parameter store accessible via a REST API.

You can pick your technologies, but we're a Python/Django shop, so we thought of the problem that way.  Just be ready to talk about why you picked the tools you did.

We're targeting this at around a 2 hour project.  If it's taking significantly longer, reach out to us-- we can always work with an in progress project for this discussion.

## Requirements

1. Provide a single API endpoint with the usual REST commands (POST/PATCH/PUT/GET/DELETE) for parameters.
1. Each parameter has a name, a value, and an indication whether or not it is a secret.
1. If a parameter is a secret, it should not be stored in plaintext

### Things Not to Worry About

* Don't spend a lot of time on how you avoid storing in plaintext-- anything is fine, we're more interested in how you approach the decision to encrypt/decrypt.
* Don't worry about users and auth, you can just skip it for this project or use something super simple.
* You don't have to worry about scalability, real world deployment models, etc.  The code is what we're interested in seeing.

### Things TO Worry About

* We view this as a chance for you to show off how you code, do the work like you would if it's your day job.
* Be sure to include documentation on how to run and test your project.

## Submission

Organize the code as you would production, include any necessary documentation and push to the `master` branch.
