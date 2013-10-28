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

1. Create a new virtualenv and activate it.
2. Install the requirements:

        $ pip install -r https://raw.github.com/sjkingo/django-project-template/master/requirements.txt

3. Create a new project using the template:

        $ export PROJECT_NAME=foo
        $ django-admin.py startproject --template https://github.com/sjkingo/django-project-template/archive/master.zip $PROJECT_NAME

It is based on the `project_template` shipped with [`stable/1.5.x`](https://github.com/django/django/tree/stable/1.5.x/django/conf/project_template).
