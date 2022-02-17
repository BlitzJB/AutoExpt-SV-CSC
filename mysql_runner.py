from pathlib import Path
import sys
import mysql.connector
import json
from subprocess import run, PIPE
from pkg_resources import to_filename

import typer
default_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'mysql_path': sys.platform == 'win32' and 'C:\\Program Files\\MySQL\\MySQL Server 5.5\\bin\\mysql.exe' or '/usr/bin/mysql'
}


def get_config():

    config = {}
    try:
        with open('config.json') as file:
            config = json.load(file)
            typer.secho(
                'Found config.json, using saved credentials..', fg='green')
    except FileNotFoundError:
        pass
    return {**default_config, **config}


def get_user_config(yes_to_all=False):
    config = {}
    typer.secho('Please enter your credentials', fg='black', bg='red')
    config['user'] = typer.prompt('Enter username', default='root')
    config['password'] = typer.prompt('Enter password', default='root')
    config['host'] = typer.prompt('Enter host', default='localhost')
    config['mysql_path'] = typer.prompt(
        'Enter mysql path', default=default_config['mysql_path'])
    save = yes_to_all or typer.confirm('Do you want to save this config?', )
    if save:
        with open('config.json', 'w') as file:
            json.dump(config, file)
    return config


def run_mysql(name: Path, yes_to_all: bool = False):
    config = get_config()
    typer.secho('{}'.format(config), fg='yellow')
    ans = yes_to_all or typer.confirm("Do you want to use this config?")
    if ans is False:
        config = get_user_config(yes_to_all)
    # split the string by ;
    with open('test.test', 'a') as file:
        for i in open(str(name)).read().split(';'):
            run([config['mysql_path'], '-u', config['user'], '-p{}'.format(config['password']), '-e', i],
                stdout=file, shell=True)
            file.write('\n')
    # cnx = mysql.connector.connect(**config)
    # cursor = cnx.cursor()
    # cursor.execute(f"source .\{name.as_posix()}")
    # data = cursor.fetchone()
    # print("Database version : %s " % data)
    # cursor.close()
    # cnx.close()
