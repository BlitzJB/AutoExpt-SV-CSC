from pathlib import Path
from typing import Optional
import typer
from experiment import Experiment


def main(
    file: Path = typer.Argument(
        ..., help="Path to the file to be processed", file_okay=True, exists=True
    ),
    title: Optional[str] = typer.Option(None),
    date: Optional[str] = typer.Option(None),
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


if __name__ == "__main__":
    typer.run(main)
