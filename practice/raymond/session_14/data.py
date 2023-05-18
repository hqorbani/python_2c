from connect import Connect
class Data(Connect):
    def __init__(self , asset_name , tm , candle_numbers, account , server_name) -> None:
        self.asset_name = asset_name
        self.tm = tm
        self.candle_numbers = candle_numbers
        super().__init__(account , server_name)
    def check_asset(self,asset_name):
        result = True
        selected=mt5.symbol_select(asset_name,True)
        if not selected:
            mt5.shutdown()
            result = False
        return result
    def get_asset(self , asset_name , tm , candle_numbers):
        rates = mt5.copy_rates_from_pos(asset_name , tm , 0 , candle_numbers)
        rates = pd.DataFrame(rates)
        rates['time'] = pd.to_datetime(rates['time'], unit = 's')
        rates['ema_8'] = ta.EMA(rates['close'] , timeperiod=8)
        rates['ema_28'] = ta.EMA(rates['close'] , timeperiod=28)
        rates['cci_30'] = ta.CCI(rates['high'], rates['low'], rates['close'], timeperiod=30)
        return rates
account , server_name = 3216545 , "metaalpari"
candle_data = Data("EURUSD" ,1, 50 ,account , server_name  )