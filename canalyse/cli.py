import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--under", is_flag=True)
def conductivity(under):
    if under:
        click.echo("hogehoge")


@cli.command()
def current():
    click.echo("fugafuga")


if __name__ == "__main__":
    cli()
