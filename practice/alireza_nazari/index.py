import MetaTrader5 as mt5
import pandas as pd
import talib as ta
class algotrader():
    def connect(self, account , server_name):
        if not mt5.initialize():
            return "initialize failed..." , mt5.last_error()
        authorized = mt5.login(account , server_name)
        if authorized:
            return True
        else:
            return "failed to connect at account",mt5.last_error()
    def check_asset(self,asset_name):
        result = True
        selected=mt5.symbol_select(asset_name,True)
        if not selected:
            mt5.shutdown()
            result = False
        return result
    def get_asset(self , asset_name , tm , candle_numbers):
        rates = mt5.copy_rates_from_pos(asset_name , tm , 0 , candle_numbers)
        
        if rates is None:
            print(mt5.last_error())
            quit()
        else:
            rates = pd.DataFrame(rates)
            rates['time'] = pd.to_datetime(rates['time'], unit = 's')
            rates['ema_8'] = ta.EMA(rates['close'] , timeperiod=8)
            rates['ema_28'] = ta.EMA(rates['close'] , timeperiod=28)
            rates['cci_30'] = ta.CCI(rates['high'], rates['low'], rates['close'], timeperiod=30)
            return rates
        
    def position(self , type_order , request):
        if type_order == "buy":
            request["type"] = mt5.ORDER_TYPE_BUY
        elif type_order == "sell":
            request["type"] = mt5.ORDER_TYPE_SELL
        else:
            print("ERROR")
        mt5.order_send(request)
    
    def do_proccess(self,asset_name , tm , candle_numbers):
        rates = self.get_asset(asset_name , tm , candle_numbers)
        print(rates)
        # last_open = rates.iloc[-1]["open"]
        # last_high = rates.iloc[-1]["high"]
        ema_28_1 = rates.iloc[-1]["ema_28"]
        ema_8_1 = rates.iloc[-1]["ema_8"]
        ema_28_2 = rates.iloc[-2]["ema_28"]
        ema_8_2 = rates.iloc[-2]["ema_8"]
        ema_28_3 = rates.iloc[-3]["ema_28"]
        ema_8_3 = rates.iloc[-3]["ema_8"]        
        cci_30_1 = rates.iloc[-1]["cci_30"]
        
        # print("ema_8: ",ema_8,"---","ema_28: ",ema_28)
    
        if ema_8_1 > ema_28_1 and ema_8_2 > ema_28_2 and ema_8_3 < ema_28_3 and cci_30_1 > 0:
            print("buy")
            request = {

            }
            self.position("buy" ,request)
        #buy
        elif ema_8_1 < ema_28_1 and ema_8_2 < ema_28_2 and ema_8_3 > ema_28_3 and cci_30_1 < 0:
            print("sell")

