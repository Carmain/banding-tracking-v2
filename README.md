# banding-tracking-v2
Version 2.0 for the banding-tracking website

Work in progress !

## What do you need ?

### Dependencies

 * [Django](https://www.djangoproject.com/download)
 * [Pyrollbar (Rollbar for python)](https://github.com/rollbar/pyrollbar)
 * gettext
   * For Linux users, the package is usually installed by default
   * For Windows, [see here](https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#gettext-on-windows])

**You can install all the dependencies with the command** `pip install -r requirements.txt`**, except for gettext (see above).**

### Configure the project
* Rename the `local_settings.py.template` into `local_settings.py`
* Inside this file, generate a band new `SECRET_KEY`
* If your interested about the Rollbar intergration, go to https://rollbar.com and get an `access_token` for this project
* Compile all the translation dictionaries : `python manage.py compilemessages`
* Migrate the database : `python3 manage.py migrate` or `python manage.py migrate` if `Python 3` is your default version

## How to lauch the project ?
 * Launch the project with `python3 manage.py runserver` or `python manage.py runserver` if `Python 3` is your default version
 * Go to http://127.0.0.1:8000 and enjoy !

## Other usefull commands
 * Generate the translation file for a specific language : ```django-admin.py makemessages -l <LANGUAGE CODE>```
 * Generate all the translation files ```django-admin.py makemessages -all```
