Sam's Django Project Template
=============================

Requires: Django 1.5.x

This `--template` sets up a new project with the following features:

* PostgreSQL for database connections.
* Sensible time zone and defaults for Brisbane, Australia.
* `local_settings.py` file to store site-specific settings, such as database, debug, etc.
* Enables the admin interface with the [Grappelli skin](https://github.com/sehmaschine/django-grappelli).
* Enables the following apps by default:
  * South
  * django-debug-toolbar

You will need to run `pip install -r project_name/requirements.txt` after `startproject` to install the dependencies.

It is based on the `project_template` shipped with [`stable/1.5.x`](https://github.com/django/django/tree/stable/1.5.x/django/conf/project_template).
