from datetime import datetime

from utils import configs
from Investment.data_factory import generate_data_source


class Market:
    def __init__(self, data_source):
        self.data_source = generate_data_source(data_source)

    def get_stock_pool(self, stock_pool_code, date):
        stocks = self.data_source.get_stock_pool(stock_pool_code, date)
        return stocks

    def get_market_data(self, codes, fields, start, end, options):
        return self.data_source.get_market_data(codes, fields, start, end, options)


market = Market(configs['default_source'])


if __name__ == '__main__':
    r = market.get_stock_pool('000300.SH', datetime.today())
    market.data_source.write2csv('hi.csv', {'col1': [1, 2, 3], 'col2': [1, 2, 3]})