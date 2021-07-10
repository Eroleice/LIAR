from datetime import datetime
from WindPy import w
import pandas as pd
import asyncio
from Investment.data_factory.base import Base


class WindData(Base):
    def __init__(self, name, config):
        super().__init__(name, config)
        w.start()
        w.isconnected()

    @classmethod
    def get_stock_pool(cls, stock_pool_code, date):
        param = f"date={date.strftime('%Y-%m-%d')};windcode={stock_pool_code}"
        res = w.wset("sectorconstituent", param)
        stocks = res.Data[1]
        return stocks

    def get_market_data(self, codes, fields, start, end, options):
        start = start.strftime('%Y-%m-%d')
        end = end.strftime('%Y-%m-%d')
        codes = ','.join(codes)
        tasks = []
        for field in fields:
            tasks.append(self.query(codes, field, start, end, options))
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(asyncio.gather(*tasks))
        return self.format_data(results)

    @staticmethod
    def format_data(results):
        # todo
        return results

    async def query(self, codes, field, start, end, options):
        res = self.query_from_db(codes, field, start, end, options)
        return res

    def query_from_db(self, codes, field, start, end, options):
        res = w.wsd(codes, field, start, end, options)
        return res

    @staticmethod
    def destroy():
        w.stop()