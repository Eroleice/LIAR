import os
import json
import pandas as pd
import numpy as np
from Leek.decision import BaseDecision


class GrowthSelection(BaseDecision):

    def __init__(self, leek, date):
        super().__init__(leek, 'growth_selection', date)


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
