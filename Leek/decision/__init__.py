from datetime import datetime
from Investment.market import market


class BaseDecision:
    def __init__(self, leek, name, date):
        self.leek = leek
        self.name = name
        self._stock_pool = []
        self.date = date

    @property
    def stock_pool(self):
        if not self._stock_pool:
            pool = self.leek.stock_pool
            self._stock_pool = market.get_stock_pool(pool, self.date)
        return self._stock_pool

    def get_market_data(self, fields, start_date, end_date, options="unit=1;Period=Q;Fill=Previous"):
        codes = self.stock_pool
        r = market.get_market_data(codes, fields, start_date, end_date, options)
        return r

    def get_leek_data(self):
        pass
