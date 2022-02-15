from pathlib import Path
from typing import Optional
import typer
from experiment import Experiment
from mysql_runner import run_mysql

app = typer.Typer()

@app.command()
def run(
    file: Path = typer.Argument(
        ..., help="Path to the file to be processed", file_okay=True, exists=True
    ),
    title: Optional[str] = typer.Option(..., prompt=True),
    date: Optional[str] = typer.Option(..., prompt=True),
    manual_output: Optional[str] = typer.Option(None),
    theme: Optional[str] = typer.Option(None),
):
    if file is not None and file.is_file():
        title = title or typer.prompt("Title")
        date = date or typer.prompt("Date")
        manual_output = manual_output or False
        Experiment(str(file), title, date, immediate = True, manual_output = manual_output, theme = theme)
    else:
        typer.secho("The file does not exist", fg="red")

@app.command()
def mysql(name: Path = typer.Argument(..., help="Path to the file to be processed", file_okay=True, exists=True),
        yes_to_all: Optional[bool] = typer.Option(False, "--y", is_flag=True, help="Skip all prompts")
    ):
    run_mysql(name, yes_to_all)
if __name__ == "__main__":
    app()
