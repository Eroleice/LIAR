import os
import pandas as pd

from Investment.data_factory.base import Base
from utils import configs


class LocalFile(Base):
    def get_stock_pool(self, *args, **kwargs):
        pass

    def get_market_data(self, *args, **kwargs):
        pass

    def query_from_db(self, **kwargs):
        url = self.config['url']
        file_name = self.parse_query(**kwargs)
        file_name = os.path.join(url, file_name)
        res = pd.read_csv(file_name)
        return res

    @classmethod
    def parse_query(cls, **kwargs):
        file_name = kwargs.get('file_name')
        return file_name

    def write2db(self, data):
        pass


if __name__ == '__main__':
    l = LocalFile('local', configs['local'])
    l.write2csv('hi.csv', {'col1': [1, 2, 3], 'col2': [1, 2, 3]})
    print(l.query_from_db(file_name='hi.csv'))