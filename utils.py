import json
import os

PATH = os.path.abspath(__file__)


def load_config():
    path = os.path.dirname(PATH)
    file = os.path.join(path, 'config.json')
    with open(file, 'r') as f:
        config = json.load(f)
    return config


configs = load_config()
