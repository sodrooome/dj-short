import click
from .utils import Script
from .callbacks import Versioning
from .commands import CreateSuperUserCommand, RunserverCommand, MigrateCommand, MakeMigrationsCommand
# from .options import GroupWithOption


@click.group()
@click.pass_context
@click.option("--version", "-v", is_flag=True, callback=Versioning, expose_value=False, is_eager=True)
def dj(ctx):
	"""Simple CLI for shortcutting Django command."""
	pass


@dj.command()
def csu():
	"""command for create superuser"""
	# command = subprocess.run("python manage.py createsuperuser", shell=True, env=env)
	if not Script:
		return
	return CreateSuperUserCommand


@dj.command()
def rsv():
	"""command for run django server"""
	# command = subprocess.run("python manage.py runserver", shell=True, env=env)
	if not Script:
		return
	return RunserverCommand


@dj.command()
def mm():
	"""command for make migrations database"""
	# command = subprocess.run("python manage.py migrate", shell=True, env=env)
	if not Script:
		return
	return MakeMigrationsCommand


@dj.command()
def m():
	"""command for migrate database"""
	# command = subprocess.run("python manage.py makemigrations", shell=True, env=env)
	if not Script:
		return
	return MigrateCommand


if __name__ == "__main__":
	dj()