from algotrader import algotrader
import json
import schedule
import time
# import pandas as pd
data = open("json/properties.json")
properties = json.load(data)
p1 = algotrader()
if p1.connect(properties["user_name"] , properties["server_name"]):
    # reates = p1.get_asset(properties["asset"] , properties["time_frame"] , properties["candle_numbers"])
    schedule.every(properties["time_period"]).seconds.do(p1.do_proccess, properties["asset"] , properties["time_frame"] , properties["candle_numbers"])
    # print(reates)
    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    print("no connection...")