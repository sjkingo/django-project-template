# Sam's Django Project Template

**Note:** The master branch contains a template for Django 3.0. If you wish to use a previous version, please
check out the appropriate branch:

* [django-2.1 branch](https://github.com/sjkingo/django-project-template/tree/django-2.1)
* [django-2.0 branch](https://github.com/sjkingo/django-project-template/tree/django-2.0)
* [django-1.10 branch](https://github.com/sjkingo/django-project-template/tree/django-1.10)
* [django-1.9 branch](https://github.com/sjkingo/django-project-template/tree/django-1.9)
* [django-1.8 branch](https://github.com/sjkingo/django-project-template/tree/django-1.8)
* [django-1.7 branch](https://github.com/sjkingo/django-project-template/tree/django-1.7)
* [django-1.6 branch](https://github.com/sjkingo/django-project-template/tree/django-1.6)

## Features

This Django project template sets up a new project with the following features:

* PostgreSQL for database connections (using `pyscopg2-binary`).
* Sensible time zone and defaults for Brisbane, Australia.
* [dj-database-url](https://github.com/kennethreitz/dj-database-url) for 12factor-inspired database URI configuration.
* Enables [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) for development.
* Flat project structure (no sub-directory called `project_name`).
* Serves static and media files when using the development server.
* Password validation is enabled for Django's auth system.
* Both WSGI and ASGI applications supported.

## Installation

Note: This will install the latest version of Django. If this is undesirable, manually download
[requirements.txt](https://raw.github.com/sjkingo/django-project-template/master/requirements.txt)
and edit accordingly.

1. Create a new virtualenv and activate it.
2. Install the requirements:

        $ pip install -r https://raw.github.com/sjkingo/django-project-template/master/requirements.txt

3. Create a new project using the template:

        $ export PROJECT_NAME=foo
        $ django-admin.py startproject --template https://github.com/sjkingo/django-project-template/archive/master.zip $PROJECT_NAME

4. Run the following to clean up the template directory and update `requirements.txt`:

        $ cd $PROJECT_NAME
        $ pip freeze > requirements.txt
        $ rm -f README.md

5. You will need to set the following environment variables:

        SECRET_KEY="<secret_key_here>"
        DATABASE_URL=postgres://<user>[:<pass>]@[<host>]/<db>

It is based on the `project_template` shipped with [`stable/3.0`](https://github.com/django/django/tree/stable/3.0.x/django/conf/project_template).

