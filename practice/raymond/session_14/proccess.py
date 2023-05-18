from data import Data
class Proccess(Data):
    def __init__(self , order_properties , asset_name) -> None:
        super().__init__(self , asset_name, tm , candle_numbers , rates)
        self.order_properties = order_properties
        self. asset_name = asset_name
        pass
    def open_position(self, order_properties):
        mt5.order_send(order_properties)
    def get_open_position_ticket(self, asset_name):
        open_positions = mt5.positions_get(symbol = asset)
        if open_positions and len(open_positions) > 0:
            return open_positions[0][0]
        else:
            return False
    def close_position(self,asset_name):
        ticket = self.get_open_position_ticket(asset)
        if ticket > 0:
            mt5.Close(asset , ticket=ticket)
            return True
        else:
            return False