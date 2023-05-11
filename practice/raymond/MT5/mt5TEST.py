import talib as ta
import schedule
import time
import json as j
import MetaTrader5 as mt5 
import pandas as pd

class mt5_connection():

    def connect(self , account , server_name):
        if not mt5.initialize():
            return "initialize failed.", mt5.last_error()
        authorized = mt5.login(account , server_name)
        if authorized:
            return True
        else:
            return "failed to connect the server or account", mt5.last_error()

    def asset(self , asset_name , tm , candle_numbers):
        rates = mt5.copy_rates_from_pos(asset_name , tm , 0 , candle_numbers)
        rates = pd.DataFrame(rates)
        rates['time'] = pd.to_datetime(rates['time'], unit = 's')
        rates['ema_8'] = ta.EMA(rates['close'] , timeperiod=8)
        rates['ema_28'] = ta.EMA(rates['close'] , timeperiod=28)
        return rates

    def do_proccess(self,asset_name , tm , candle_numbers):
        rates = self.asset(asset_name , tm , candle_numbers)
        last_open = rates.iloc[-1]["open"]
        print(rates)
        return last_open
        
x = open("get_info.json")
properties = j.load(x)
p1 = mt5_connection()
if p1.connect(properties["account"] , properties["server_name"]):
    schedule.every(properties["time_period"]).seconds.do(p1.do_proccess, properties["asset_name"] , properties["tm"] , properties["candle_numbers"])
    while True:
        schedule.run_pending()
        time.sleep(1)