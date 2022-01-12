import click


@click.group()
def live():
    click.echo(">> Live")


@live.command()
def eat():
    click.echo(">>> Eating")


@live.command()
def play():
    click.echo(">>> Playing")
