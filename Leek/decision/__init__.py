import os
import json
import pandas as pd
from Investment.market import market


class BaseDecision:
    def __init__(self, leek, name, date):
        self.leek = leek
        self.name = name
        self._stock_pool = []
        self.date = date
        self.market = market
        self._rules = []

    @property
    def stock_pool(self):
        if not self._stock_pool:
            pool = self.leek.stock_pool
            self._stock_pool = self.market.get_stock_pool(pool, self.date)
        return self._stock_pool

    def get_market_data(self, start_date, end_date, options="unit=1;Period=Q;Fill=Previous"):
        codes = self.stock_pool
        fields = self.get_fields()
        r = self.market.get_market_data(codes, fields, start_date, end_date, options)
        return r

    def get_leek_data(self):
        pass

    @property
    def rules(self):
        if not self._rules:
            path = os.path.abspath(__file__)
            path = os.path.dirname(path)
            file = os.path.join(path, self.name + '.json')
            with open(file, 'r') as f:
                self._rules = json.load(f)
        return self._rules

    def get_fields(self):
        fields = set()
        fields.add('close')     # 收盘价
        fields.add('ev')        # 市值
        for r in self.rules:
            a = r['A']
            b = r['B']
            if a['type'] == 'field':
                fields.add(a['value'])
            if b['type'] == 'field':
                fields.add(b['value'])
        return fields

    def apply_rules(self, data):
        results = {}
        for code, df in data.items():
            ans = True
            for rule in self.rules:
                a = rule['A']
                b = rule['B']
                a_value = df.iloc[a['time']][a['value']] if a['type'] == 'field' else a['value']
                b_value = df.iloc[b['time']][b['value']] if b['type'] == 'field' else b['value']
                if pd.isna(a_value) or pd.isna(b_value):
                    ans = False
                    break
                op = rule['op']
                ans = self.check(op, a_value, b_value)
                if not ans:
                    break
            if ans:
                results[code] = df
        return results

    @staticmethod
    def check(op, a, b):
        if op == '<':
            ans = a < b
        elif op == '<=':
            ans = a <= b
        elif op == '>':
            ans = a > b
        elif op == '>=':
            ans = a >= b
        elif op == '=':
            ans = a == b
        elif op == '!=':
            ans = a != b
        else:
            raise Exception(f'invalid operation: {op}')
        return ans

