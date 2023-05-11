from algotrader import algotrader

server_name = "MetaQuotes-Demo"
account = 5012265195

p1 = algotrader()
if p1.connect(account , server_name):
    reates = p1.get_asset('EURUSD' , 1 , 10)
    print(reates)
else:
    print("no connection...")