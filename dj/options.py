import click


class GroupWithCommandOptions(click.Group):
    """Class for override grouping method in click"""

    def add_command(self, cmd, name=None):
        click.Group.add_command(self, cmd, name=name)

        # add another params into group option
        for param in self.params:
            cmd.params.append(param)

        # invoke command so the grouping method
        # could be add another params in option.
        # based on click documentation, grouping method
        # skips directly for add another param
        # in option method, so in this case i'm trying
        # to change the invoke method so that can be used
        cmd.invoke = self.invoke_group_command(cmd.invoke)
        self.invoke_without_command = True


class GroupWithOption(GroupWithCommandOptions):
    """Inherit class"""

    def invoke_group_command(self, original_invoke, ctx):
        # this function should be something like,
        # inserting new param name into option command
        # so that can be used later in grouping method
        # but, it turns out it doesn't work
        # WIP: fix this code
        ctx.object = dict(_params=dict())
        for param in self.params:
            name = param.name
            ctx.object["_params"][name] = ctx.params[name]
            del ctx.params[name]

        params = ctx.params
        ctx.params = ctx.object["_params"]
        self.invoke(ctx)
        ctx.params = ctx.params
        original_invoke(ctx)
        return self.invoke_group_command
