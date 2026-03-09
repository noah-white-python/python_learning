name = "传智播客"
stock_price = 19.99
stock_code = 123456
stock_price_daily_growth_factor = 1.2
growth_days = 7
print("公司:%s,股票代码%d,当前股价%.2f"%(name,stock_code,stock_price))
print(      "每日增长系数是%.2f，经过%d天增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,1.2**7*stock_price))



print("请告诉我你是谁：")
name = input()
print("你的名字是%s" % name)
