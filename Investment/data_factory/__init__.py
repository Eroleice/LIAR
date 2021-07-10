from utils import configs

from .wind import WindData
from .local_file import LocalFile


def generate_data_source(name):
    if name == 'local':
        return LocalFile('local', configs['data_source']['local'])
    elif name == 'wind':
        return WindData('wind', configs['data_source']['wind'])
