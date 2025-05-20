import typer

from cli.run import app as run_app

app = typer.Typer(name='Access project command line interface')

app.add_typer(run_app, name='run')


if __name__ == '__main__':
    app()
