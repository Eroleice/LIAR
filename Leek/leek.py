import numpy as np
import pandas as pd
from datetime import datetime
from collections import defaultdict

from Leek.exceptions import TransferException, TradeException


PERIOD = ['D', 'W', 'M', 'Q', 'S', 'A']


class Leek:
    def __init__(self, leek_id, stock_pool='000300.SH'):
        self.leek_id = leek_id
        self.account = Account()
        #todo: 考虑同时选择两个或以上的指数作为池子，例如同时选择沪深300+上证180，调取两个指数的成分股并去重
        self.stock_pool = stock_pool

    def make_decision(self, date):
        pass

    def trade(self):
        t = Trade()
        try:
            self.account.trade(t)
        except Exception as e:
            print(e)


class Account:
    def __init__(self):
        self._balance = 0
        self.holdings = defaultdict(int)  # {share_code: share_amounts}
        self.records = []

    @property
    def balance(self):
        return self._balance

    def _check_balance(self, money):
        return self.balance + money >= 0

    def _check_holdings(self, trade):
        code = trade.stock_code
        return self.holdings[code] - trade.amount >= 0

    def transfer(self, money):
        if not self._check_balance(money):
            raise TransferException(self.balance, money)
        self._balance += money

    def trade(self, trade):
        money = trade.price * trade.amount
        if trade.direction == Trade.LONG:
            if not self._check_balance(money):
                raise TradeException(self, trade)
            self.holdings[trade.stock_code] += trade.amount
            self._balance -= money
        elif trade.direction == Trade.SHORT:
            if not self._check_holdings(trade):
                raise TradeException(self, trade)
            self.holdings[trade.stock_code] -= trade.amount
            self._balance += money

        self.records.append(trade.info)


class Trade:
    __slots__ = ['date', 'stock_code', 'amount', 'price', 'direction', 'method', 'credit_trading', 'type']
    LONG = 'Long'
    SHORT = 'Short'

    def __init__(self):
        self.stock_code = None
        self.price = 0
        self.amount = 0
        self.date = datetime.today()
        self.direction = Trade.LONG
        self.method = 'BuySell'
        self.credit_trading = 'No'
        self.type = 'flow'

    @property
    def info(self):
        record = []
        for k in ['date', 'stock_code', 'amount', 'price', 'direction', 'method', 'credit_trading', 'type']:
            record.append(getattr(self, k))
        return record


if __name__ == '__main__':
    a = Account()
    a.transfer(-5)
