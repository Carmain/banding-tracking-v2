# banding-tracking-v2
Version 2.0 for the banding-tracking website

Work in progress !

## What do you need ?
* [Django](https://www.djangoproject.com/download/)
* gettext
    * For Linux users, the package is usually installed by default
    * For Windows, [see here](https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#gettext-on-windows])

## How to lauch the project ?

 * Compile all the translation dictionaries : ```python manage.py compilemessages```
 * Migrate the database : ```python manage.py migrate```
 * Launch the project : ```python manage.py runserver```

## Other usefull commands
 * Generate the translation file for a specific language : ```django-admin.py makemessages -l <LANGUAGE CODE>```
