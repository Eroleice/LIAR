from WindPy import w

w.start() # 默认命令超时时间为120秒，如需设置超时时间可以加入waitTime参数，例如waitTime=60,即设置命令超时时间为60秒  

w.isconnected() # 判断WindPy是否已经登录成功


# 获取日时间序列函数WSD
# 支持股票、债券、基金、期货、指数等多种证券的基本资料、股东信息、市场行情、证券分析、预测评级、财务数据等各种数据。wsd可以支持取 多品种单指标 或者 单品种多指标 的时间序列数据。
history_data = w.wsd("000009.SZ,000012.SZ,000021.SZ", "roe_deducted", "2015-01-01", "2020-12-31", "Period=Q", usedf=True)
# returnType表示到期收益率计算方法，PriceAdj表示债券价格类型‘
print(history_data)





w.stop() # 当需要停止WindPy时，可以使用该命令
         # 注： w.start不重复启动，若需要改变参数，如超时时间，用户可以使用w.stop命令先停止后再启动。
         # 退出时，会自动执行w.stop()，一般用户并不需要执行w.stop 