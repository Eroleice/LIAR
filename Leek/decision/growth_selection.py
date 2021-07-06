
from Leek.decision import BaseDecision


class GrowthSelection(BaseDecision):

    def __init__(self, leek, date):
        super().__init__(leek, 'growth selection', date)

# 选股逻辑：
# 1. 当期 operatecashflow_ttm 大于0
# 2. 90天前 operatecashflow_ttm 大于0
# 3. 180天前 operatecashflow_ttm 大于0
# 4. 当期 fa_roe_avg 大于20
# 5. 360天前 fa_roe_avg 大于10
# 6. 720天前 fa_roe_avg 大于10
# 7. 当期 pb_lf 小于50
# 8. 当期 fa_npgr_ttm 大于15
# 9. 90天前 fa_npgr_ttm 大于15
# 10. 180天前 fa_npgr_ttm 大于15
# 11. 当期 fa_npgr_ttm 小于 90天前 fa_npgr_ttm 
# 12. 当期 ipo_listdays 大于180

# if __name__ == '__main__':
#     from datetime import datetime, timedelta
#     a = GrowthSelection()
#     a.stock_pool = '000300.SH'
#     g = GrowthSelection(a, datetime.today())
#     r = g.get_market_data(fields=["operatecashflow_ttm", "profit_ttm"], start_date=datetime.today()-timedelta(days=1000), end_date=datetime.today())
#     for k, v in r.items():
#         print(k, v)
