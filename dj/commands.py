import os
import subprocess


class BaseCommand(object):
    """Base constructor for Django command"""

    def __init__(self, env=None, shell=True):
        if env is None:
            env = dict(os.environ, **{"PYTHONUNBUFFERED": "1"})
        self.env = env
        self.shell = shell


class CreateSuperUserCommand(BaseCommand):
    def command(self):
        return subprocess.run("python manage.py createsuperuser", self.env, self.shell)


class RunserverCommand(BaseCommand):
    def command(self):
        return subprocess.run("python manage.py runserver", self.env, self.shell)


class MigrateCommand(BaseCommand):
    def command(self):
        return subprocess.run("python manage.py migrate", self.env, self.shell)


class MakeMigrationsCommand(BaseCommand):
    def command(self):
        return subprocess.run("python manage.py makemigrations", self.env, self.shell)