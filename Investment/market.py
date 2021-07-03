from datetime import datetime
from WindPy import w
import pandas as pd
import asyncio
import time


class Market:
    def __init__(self):
        w.start()
        w.isconnected()

    @classmethod
    def get_stock_pool(cls, stock_pool_code, date):
        param = f"date={date.strftime('%Y-%m-%d')};windcode={stock_pool_code}"
        res = w.wset("sectorconstituent", param)
        stocks = res.Data[1]
        return stocks

    @classmethod
    def get_market_data(cls, codes, fields, start, end, options):
        start = start.strftime('%Y-%m-%d')
        end = end.strftime('%Y-%m-%d')
        codes = ','.join(codes)
        tasks = []
        for field in fields:
            tasks.append(cls.query(codes, field, start, end, options))
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(asyncio.gather(*tasks))

        return cls.format_data(results)

    @staticmethod
    def format_data(results):
        # todo
        return results

    @staticmethod
    async def query(codes, field, start, end, options):
        res = w.wsd(codes, field, start, end, options)
        return res

    @staticmethod
    def destroy():
        w.stop()


market = Market()


if __name__ == '__main__':
    r = market.get_stock_pool('000300.SH', datetime.today())
    market.destroy()