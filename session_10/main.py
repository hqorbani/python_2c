from algotrader import algotrader
import json
import schedule
import time
import MetaTrader5 as mt5
# import pandas as pd
data = open("json/properties.json")
properties = json.load(data)
p1 = algotrader()
if p1.connect(properties["user_name"] , properties["server_name"]) and p1.check_asset(properties["asset"]):
    asset_info = mt5.symbol_info_tick(properties["asset"])._asdict()
    print(type(asset_info))
    # lot = 0.1
    price = mt5.symbol_info_tick(properties["asset"]).ask
    # point = mt5.symbol_info(properties["asset"]).point
    # deviation = 20
    # print(price)
    # request = {
    #     "action": mt5.TRADE_ACTION_DEAL,
    #     "symbol": properties["asset"],
    #     "volume": lot,
    #     "type": mt5.ORDER_TYPE_BUY,
    #     "price": price,
    #     "sl": price - 100 * point,
    #     "tp": price + 100 * point,
    #     "deviation": deviation,
    #     "magic": 234000,
    #     "comment": "python script open",
    #     "type_time": mt5.ORDER_TIME_GTC,
    #     "type_filling": mt5.ORDER_FILLING_RETURN,
    # }
    # p1.open_position(request)
    schedule.every(properties["time_period"]).seconds.do(p1.do_proccess, properties["asset"] , properties["time_frame"] , properties["candle_numbers"])
    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    print("no connection...")