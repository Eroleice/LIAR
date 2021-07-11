import os
import pandas as pd
from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self, name, config):
        self.name = name
        self.config = config

    @abstractmethod
    def query_from_db(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_stock_pool(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_market_data(self, *args, **kwargs):
        pass

    # todo optimize with multi-thread
    def write2csv(self, name, data):
        path = self.config['url']
        if not os.path.exists(path):
            os.makedirs(path)
        file_name = os.path.join(path, name)
        # write to file
        if isinstance(data, pd.DataFrame):
            data.to_csv(file_name, index=False)
        else:
            pd.DataFrame.from_dict(data).to_csv(file_name, index=False)