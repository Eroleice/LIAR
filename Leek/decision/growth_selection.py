
from Leek.decision import BaseDecision


class GrowthSelection(BaseDecision):

    def __init__(self, leek, date):
        super().__init__(leek, 'growth selection', date)


# if __name__ == '__main__':
#     from datetime import datetime, timedelta
#     a = GrowthSelection()
#     a.stock_pool = '000300.SH'
#     g = GrowthSelection(a, datetime.today())
#     r = g.get_market_data(fields=["operatecashflow_ttm", "profit_ttm"], start_date=datetime.today()-timedelta(days=1000), end_date=datetime.today())
#     for k, v in r.items():
#         print(k, v)
