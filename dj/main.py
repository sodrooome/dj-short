import os
import click
import subprocess
from .utils import Script
from .callbacks import Versioning
# from .options import GroupWithOption

# global variables for python environment
env = dict(os.environ, **{"PYTHONUNBUFFERED": "1"})

@click.group()
@click.pass_context
@click.option("--version", "-v", is_flag=True, callback=Versioning, 
			 expose_value=False, is_eager=True)
def dj(ctx):
	"""Simple CLI for shortcutting Django command."""
	pass

@dj.command()
def csu():
	"""command for create superuser"""
	command = subprocess.run("python manage.py createsuperuser", shell=True, env=env)
	if not Script:
		return
	else:
		return command

@dj.command()
def rsv():
	"""command for run django server"""
	command = subprocess.run("python manage.py runserver", shell=True, env=env)
	if not Script:
		return
	else:
		return command

@dj.command()
def mm():
	"""command for make migrations database"""
	command = subprocess.run("python manage.py migrate", shell=True, env=env)
	if not Script:
		return
	else:
		return command

@dj.command()
def m():
	"""command for migrate database"""
	command = subprocess.run("python manage.py makemigrations", shell=True, env=env)
	if not Script:
		return
	else:
		return command

if __name__ == "__main__":
	dj()