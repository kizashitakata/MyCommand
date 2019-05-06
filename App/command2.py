import click

@click.group()
def main():
    pass

@main.command()
def one():
    click.echo('処理1')

@main.command()
def two():
    click.echo('処理2')
