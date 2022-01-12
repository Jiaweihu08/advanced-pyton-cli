import click


@click.group()
def study():
    click.echo(">> Studying")


@study.command()
def do_a_mooc():
    click.echo(">>> Doing a MOOC")


@study.command()
def read():
    click.echo(">>> Reading a book")