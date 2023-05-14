import talib as ta
import schedule
import time
import json as j
import MetaTrader5 as mt5 
import pandas as pd
positions_dic = {}
x = open("get_info.json")
properties = j.load(x)
class mt5_connection():
    def __init__(self , account , server_name) -> None:
        self.account = properties["account"]
        self.server_name = properties["server_name"]

    def connect(self, account , server_name):
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
        rates['cci_30'] = ta.CCI(rates['high'], rates['low'], rates['close'], timeperiod=30)
        return rates
    
    def check_asset(self,asset_name):
        self.asset_name = properties["asset_name"]
        result = True
        selected=mt5.symbol_select(asset_name,True)
        if not selected:
            mt5.shutdown()
            result = False
        return result

    def open_position(self, order_properties):
        mt5.order_send(order_properties)
    
    def get_open_position_ticket(self, asset):
        self.asset = "NZDSGD"
        open_positions = mt5.positions_get(symbol = self.asset)
        if open_positions and len(open_positions) > 0:
            return open_positions[0][0]
        else:
            return False
    
    def close_position(self,asset):
        ticket = self.get_open_position_ticket("NZDSGD")
        if ticket > 0:
            mt5.Close(asset , ticket=ticket)
            return True
        else:
            return False

    def do_proccess(self,asset_name , tm , candle_numbers):
        rates = self.asset(asset_name , tm , candle_numbers)
        last_open = rates.iloc[-1]["open"]
        ema_28_1 = rates.iloc[-1]["ema_28"]
        ema_8_1 = rates.iloc[-1]["ema_8"]
        ema_28_2 = rates.iloc[-2]["ema_28"]
        ema_8_2 = rates.iloc[-2]["ema_8"]
        cci_30_1 = rates.iloc[-1]["cci_30"]

        if ema_8_1 > ema_28_1 and ema_8_2 > ema_28_2 and cci_30_1 > 0:
            if len(positions_dic) == 0:
                price = mt5.symbol_info_tick(properties["asset_name"]).ask
                point = mt5.symbol_info(properties["asset_name"]).point
                lot = 0.3
                deviation = 20
                order_properties = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": properties["asset_name"],
                    "volume": lot,
                    "type": mt5.ORDER_TYPE_BUY,
                    "price": price,
                    "sl": price - 100 * point,
                    "tp": price + 100 * point,
                    "deviation": deviation,
                    "magic": 234000,
                    "comment": "python script open",
                    "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_RETURN,
                }
                positions_dic["position: "] = "1"
                open_position(order_properties)
                print(buy)
            else:
                print("a position is alredy running.")
        elif ema_8_1 < ema_28_1 and ema_8_2 < ema_28_2 and cci_30_1 < 0:
            if len(positions_dic) == 1:
                close_position("NZDSGD")
                print("sell")

account = properties["account"]
server_name = properties["server_name"]
p1 = mt5_connection(account , server_name)
if p1.connect(properties["account"] , properties["server_name"]) and p1.check_asset(properties["asset_name"]):
    asset_info = mt5.symbol_info_tick(properties["asset_name"])._asdict()
    price = mt5.symbol_info_tick(properties["asset_name"]).ask
    schedule.every(properties["time_period"]).seconds.do(p1.do_proccess, properties["asset_name"] , properties["tm"] , properties["candle_numbers"])
    
    while True:
        schedule.run_pending()
        time.sleep(1)