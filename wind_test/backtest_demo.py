from WindPy import w

PortfolioName = "LIAR"

w.start() # 默认命令超时时间为120秒，如需设置超时时间可以加入waitTime参数，例如waitTime=60,即设置命令超时时间为60秒  

w.isconnected() # 判断WindPy是否已经登录成功

# 存钱
w.wupf(PortfolioName, "20210703", "CNY", "1000000", "1","Direction=Long;Method=BuySell;CreditTrading=No;type=flow")

# 取钱
w.wupf(PortfolioName, "20210703", "CNY", "-1000000", "1","Direction=Long;Method=BuySell;CreditTrading=No;type=flow")