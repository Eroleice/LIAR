
class TransferException(Exception):
    def __init__(self, balance, money):
        self.balance = balance
        self.money = money

    def __str__(self):
        return f"Transfer Failed: Insufficient Balance!\nCurrent:{self.balance} \nCharging:{-self.money}"


class TradeException(Exception):
    def __init__(self, account, trade):
        self.account = account
        self.trade = trade

    def __str__(self):
        if self.trade.direction == self.trade.LONG:
            msg = f'Trade Failed: Insufficient Balance!\nCurrent:{self.account.balance} \nCharging:{self.trade.amount*self.trade.price}'
        elif self.trade.direction == self.trade.SHORT:
            code = self.trade.stock_code
            msg = f'Trade Failed: Insufficient Holdings:{code}!\nCurrent:{self.account.holdings[code]} \nSelling:{self.trade.amount}'
        else:
            msg = 'go fuck yourself'
        return msg

