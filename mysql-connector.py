import mysql.connector
import json

def get_config():
    default_config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost', }
    config = {}
    try:
        with open('config.json') as file:
            config = json.load(file)
    except FileNotFoundError:
        pass
    return {**default_config, **config}
