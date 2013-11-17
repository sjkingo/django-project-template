Sam's Django Project Template
=============================

This Django project template sets up a new project with the following features:

* PostgreSQL for database connections.
* Sensible time zone and defaults for Brisbane, Australia.
  * Note that internationalization and time zone-aware datetimes are disabled!
* `local_settings.py` file to store site-specific settings. This allows `settings.py` to be committed to
  version control without exposing passwords or keys.
* Enables the admin interface with the [Grappelli skin](https://github.com/sehmaschine/django-grappelli).
* Enables the following apps by default:
  * South
  * django-debug-toolbar
  * django-grappelli

Installation
------------

Note: This will install the latest stable version of Django (at the time of writing, 1.6). If this is undesirable,
manually download [requirements.txt](https://raw.github.com/sjkingo/django-project-template/master/requirements.txt)
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
        $ chmod +x manage.py

It is based on the `project_template` shipped with [`stable/1.5.x`](https://github.com/django/django/tree/stable/1.5.x/django/conf/project_template).
