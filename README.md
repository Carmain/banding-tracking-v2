# banding-tracking-v2

![Python version](https://img.shields.io/badge/Python_version-3.8.1-306998.svg?logo=Python&logoColor=white)
![Project version](https://img.shields.io/badge/Project_version-0.0.1-ffd43b.svg)

![Bootstrap version](https://img.shields.io/badge/Bootstrap_version-3.4.1-563d7c.svg?logo=Bootstrap&logoColor=white)

`Banding-tracking` is the second version of a web app used by citizens and birdwatchers to save observations and get the life track of banded kentish plovers as part of a program on this specie in Normandy (France).

## How to install the project

### About the python dependencies

Your probably will need to install `gettext` ([https://www.gnu.org/software/gettext/](https://www.gnu.org/software/gettext/)) for the translations. For Linux users, the package is usually installed by default. For Windows, [see here](https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#gettext-on-windows]).

#### Important information before begin

Please visit the documentation of WeazyPrint. WeazyPrint depends on packages which need to be installed separately. See platform-specific instructions for Linux, OS X and Windows in the documentation.

**P.S** : On Ubuntu 16.04, you will probably need to install libffi-dev too.

### Installation roadmap

1. Install all the dependencies with `pipenv` :

   ```bash
   pipenv install # For production
   pipenv install --dev # For development
   ```

2. Install the front dependencies

   ```bash
   yarn install
   ```

3. Add the `.env` file & fill all the informations needed (`ROLLBAR_ACCESS_TOKEN` is optionnal)

   ```bash
   cp .env.example .env
   ```

4. Compile all the translation dictionaries

   ```bash
   python manage.py compilemessages
   ```

5. Migrate the database

   ```bash
   python manage.py migrate
   ```

6. Load seeds if needed

   ```bash
   python manage.py loaddata seeders/*
   ```

### Retreive a rollbar access token

Initiate the Rollbar intergration :

- Go to [https://rollbar.com](https://rollbar.com) and get an access token for this project
- Set it in `ROLLBAR_ACCESS_TOKEN`

## How to lauch the project

In a terminal :

```bash
python manage.py runserver
```
