from enum import Enum

import typer


app = typer.Typer(name='Project run commands')


class RunMode(Enum):
    local = 'local'
    docker = 'docker'


@app.command(name='app')
def project(mode: RunMode | None = 'local') -> None:
    """
    Run the application
    """