import click


@click.group()
def work():
    click.echo(">> Working")


@work.command()
def program():
    click.echo(">>> Programming")


@work.command()
def take_order():
    click.echo(">>> Taking a order")
