import os
import sys


class Script(object):
	def __init__(self, name="manage.py") -> bool:
		self.name = name

	def find_script(self) -> bool:
		"""Method for searching manage.py file"""
		paths = []
		directory = os.getcwd()
		while True:
			django_path = os.path.join(directory, self.name)
			paths.append(django_path)
			if os.path.exists(django_path):
				return django_path

			django_base_path = os.path.dirname(directory)
			if django_base_path == directory:
				# why this exit doesn't work?
				sys.exit("No manage.py file or something like Django environment is exists in here.")
			directory = django_base_path