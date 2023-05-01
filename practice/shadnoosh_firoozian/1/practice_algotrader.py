import MetaTrader5 as mt5
import pandas as pd
import talib as ta
import gtts  
from playsound import playsound  
class algotrader():
    def connect(self, account , server_name):
        if not mt5.initialize():
            return "initialize failed..." , mt5.last_error()
        authorized = mt5.login(account , server_name)
        if authorized:
            return True
        else:
            return "failed to connect at account",mt5.last_error()
    def get_asset(self , asset_name , tm , candle_numbers):
        rates = mt5.copy_rates_from_pos(asset_name , tm , 0 , candle_numbers)
        if rates is None:
            print(mt5.last_error())
            quit()
        else:
            rates = pd.DataFrame(rates)
            rates['time'] = pd.to_datetime(rates['time'], unit = 's')
            rates['ema_8'] = ta.EMA(rates['close'] , timeperiod = 8)
            rates['ema_28'] = ta.EMA(rates['close'] , timeperiod = 28)
            return rates
    def do_proccess(self, asset_name , tm , candle_numbers):
        rates = self.get_asset(asset_name , tm , candle_numbers)
        print(rates)
        ema_28_1 = rates.iloc[-1]["ema_28"]
        ema_8_1 = rates.iloc[-1]["ema_8"]
        ema_28_2 = rates.iloc[-2]["ema_28"]
        ema_8_2 = rates.iloc[-2]["ema_8"]
        text_buy= gtts.gTTS("it is time to buy")
        text_buy.save("buy.mp3")
        text_sell= gtts.gTTS("it is time to sell")
        text_sell.save("sell.mp3")
        if ema_8_1 > ema_28_1 and ema_8_2 > ema_28-2:
            playsound("buy.mp3")
        else:
            playsound("sell.mp3")
              

