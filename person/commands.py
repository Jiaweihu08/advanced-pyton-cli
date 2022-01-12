import click

from person.work import work
from person.live import live
from person.study import study


@click.group()
def cli():
    click.echo("> A Person does:")


cli.add_command(work)
cli.add_command(live)
cli.add_command(study)


if __name__ == '__main__':
    cli()
