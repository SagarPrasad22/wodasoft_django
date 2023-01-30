# wodasoft_django
## Django i18n support project

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

It is a Django based web application where multi language support is demonstrated using model

## Objective

- When Django’s LANGUAGES parameter is updated (e.g. one more language is added/removed), a corresponding field must be added/removed automatically;
- Default language field must be required, it must not be allowed for a user to save any model without default language value specified;
- Dynamically add item and it's translations as JSON from Django admin
- Also, load initial item and it's translations as JSON using Django Fixtures

## Installation

To install and run this application first go to project folder and run below mentioned commands

Run below commands to create virtual environment
```sh
sudo api install virtualenv
virtualenv venv
```

Run below commands to install required libraries and migrate database tables

```sh
pip install -r requirements.txt
```

If you are not using provided sqlite database file

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata article_data.json
python manage.py createsuperuser
```
And enter your desired Username, Email & Password for super user 

## Default credentials [For Super admin]


| Username | Password |
| ------ | ------ |
| admin@gmail.com | 12345678 |

## Q&A

**Pros:**
- By bypassing Django's default i18n representation of locale lc message render where we have to write text translations on separate language po files, now we can store the text translations on model as JSON data which is more convenient and easy to use with Django Admin.


**Cons:**
- Adding text translations of different languages manually still a tedious task for the user.


**Improvements:**
- We can use python libraries like "Translate", by which we can translate any text to required languages automatically.
- So, that the user don't have to manually translate text and store it to database.


## License

MIT

**Free Software, Hell Yeah!**