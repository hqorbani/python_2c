import MetaTrader5 as mt5
import pandas as pd
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
            return rates
    def do_proccess(self,asset_name , tm , candle_numbers):
        rates = self.get_asset(asset_name , tm , candle_numbers)
        # print(rates)
        last_open = rates.iloc[-1]["open"]
        ema_28 = rates.iloc[-1]["ema_28"]
        ema_8 = rates.iloc[-1]["ema_8"]
        print("last_open: ",last_open)
        if ema_8 > ema_28:
            pass
        #buy
        else:
            pass


