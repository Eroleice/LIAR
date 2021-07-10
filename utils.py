import yaml
import os

PATH = os.path.abspath(__file__)


def load_config():
    path = os.path.dirname(PATH)
    file = os.path.join(path, 'config.yml')
    with open(file, 'r') as f:
        config = yaml.safe_load(f)
    return config


configs = load_config()
