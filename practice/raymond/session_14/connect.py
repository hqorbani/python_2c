import MetaTrader5 as mt5
class Connect:
    def __init__(self, account , server_name) -> None:
        self.account = account
        self.server_name = server_name
    def connect(self):
        if not mt5.initialize():
            return "initialize failed.", mt5.last_error()
        authorized = mt5.login(self.account , self.server_name)
        print(authorized)
        if authorized:
            return True
        else:
            return "failed to connect the server or account", mt5.last_error()

conn = Connect(68263282 , "MetaQuotes-Demo")
print(conn.connect())
