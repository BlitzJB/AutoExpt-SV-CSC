from pathlib import Path
import mysql.connector
import json
from subprocess import run, PIPE
from pkg_resources import to_filename

import typer

def get_config():
    default_config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost', }
    config = {}
    try:
        with open('config.json') as file:
            config = json.load(file)
            typer.secho('Found config.json, using saved credentials..', fg='green')
    except FileNotFoundError:
        pass
    return {**default_config, **config}

def get_user_config():
    config = {}
    typer.secho('Please enter your credentials', fg='black', bg='red')
    config['user'] = typer.prompt('Enter username', default='root')
    config['password'] = typer.prompt('Enter password', default='root')
    config['host'] = typer.prompt('Enter host', default='localhost')
    save = typer.confirm('Do you want to save this config?', )
    if save:
        with open('config.json', 'w') as file:
            json.dump(config, file)
    return config
def run_mysql(name: Path):
    config = get_config()
    typer.secho('{}'.format(config), fg='yellow')
    ans = typer.confirm("Do you want to use this config?")
    print(ans)
    if ans is False:
        config = get_user_config()
    execute_file_name = f'exeute_{str(name)}.sql'
    with open(execute_file_name, 'w+') as file:
        file.write(f'source {str(name)}; exit;')
        process = run(['mysql', '-u', config['user'], '-p', config['password']], stdout=PIPE, stdin=file, encoding='utf-8')
        output = process.stdout
        error = process.stderr
        typer.secho(output, fg='green')
        typer.secho(error, fg='red')
        # cnx = mysql.connector.connect(**config)
        # cursor = cnx.cursor()
        # cursor.execute("source %s", (name.as_posix(),))
        # data = cursor.fetchone()
        # print("Database version : %s " % data)
        # cursor.close()
        # cnx.close()