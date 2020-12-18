## Django CLI

Simple python CLI program for shortcutting Django command

## Usage

You can install this CLI with :
```sh
pip install dj-short
```

And after that, on your root Django project you can use this CLI by executing `dj` and add following commands like :

- `csu` for create a new superuser (based on `python manage.py createsuperuser`)
- `rsv` for run the django server (based on `python manage.py runserver`)
- `mm` for make a migrations for database (based on `python manage.py makemigrations`)
- `m` for migrate the database (based on `python manage.py migrate`)

## Why this package (even) exist?

Cause i'm lazy and little bit tired for too much typing in Django command. To be honest, i also don't really understand why django command management can't be shortened like in Ruby on Rails (the only way is to use a shortened django command is make a custom bash script or configuration in existing files such as `.ini` or `.toml`)

## Shortcomings

This CLI is temporarily unable to dynamically add new arguments to each existing command. Example: all arguments or option is limited and it's based on default parameter that provided by Django, just like when we're going to running django server specifically on a particular port, we cannot change the port number / addresses. 