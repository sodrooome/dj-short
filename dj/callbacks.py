import click
from .version import get_version


class Versioning(object):
	def __init__(self, ctx, param, value):
	    self.ctx = ctx
	    self.param = param
	    self.value = value

	@property
	def version(self):
		if not self.value or self.ctx.resilient_parsing:
			return
		click.echo(get_version())
		self.ctx.exit()
