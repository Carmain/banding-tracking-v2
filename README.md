# banding-tracking-v2
Version 2.0 for the banding-tracking website


## Before begin
 * All the commands work with `Python 3`. If `Python 3` is your default version, just start all the commands with `python`
 * You can install all the dependencies for this project with the command `pip install -r requirements.txt`, except for gettext (see below).

## What do you need ?

### Dependencies

#### Mandatory
 * [Django](https://www.djangoproject.com/download)
 * [gettext](https://www.gnu.org/software/gettext/)
   * For Linux users, the package is usually installed by default
   * For Windows, [see here](https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#gettext-on-windows])

#### Optionnal (but usefull for the dev & debug)
 * [django-extensions](https://github.com/django-extensions/django-extensions)
 * [Werkzeug](http://werkzeug.pocoo.org/)
 * [Pyrollbar (Rollbar for python)](https://github.com/rollbar/pyrollbar)

### Configure the project
 * Rename the `local_settings.template` into `local_settings.py`
 * Inside this file, generate a brand new `SECRET_KEY`
 * Initiate the Rollbar intergration :
   * Go to https://rollbar.com and get an access token for this project
   * Set it in `ROLLBAR_ACCESS_TOKEN`
 * Compile all the translation dictionaries : `python3 manage.py compilemessages`
 * Migrate the database : `python3 manage.py migrate`

## How to lauch the project ?
 * Launch the project with `python3 manage.py runserver`
 * For a better experience you could launch the project with `python3 manage.py runserver_plus` but you need to install `django-extensions` & `Werkzeug` (see the **Dependecies** section)
 * Go to http://127.0.0.1:8000 and enjoy !

## Other usefull commands
 * Generate the translation file for a specific language : ```django-admin.py makemessages -l <LANGUAGE CODE>```
 * Generate all the translation files ```django-admin.py makemessages -all```

 * Flush database : `python manage.py flush`
 * Seed database : `python manage.py loaddata locations.json observers.json plovers.json`
