import click

class Versioning(object):
	def __init__(self, ctx, param, value):
		self.ctx = ctx
		self.param = param
		self.value = value

	def version(self):
		if not self.value or self.ctx.resilient_parsing:
			return
		click.echo("Django CLI v0.1.0")
		self.ctx.exit()