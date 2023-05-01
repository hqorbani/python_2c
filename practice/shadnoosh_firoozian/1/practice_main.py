from practice_algotrader import algotrader
import json
import schedule
import time
info = open("data.json")
data = json.load(info)
p1 = algotrader()
if p1.connect(data["user_name"] , data["server_name"]):
    schedule.every(data["time_period"]).seconds.do(p1.do_proccess, data["asset"] , data["time_frame"] , data["candle_numbers"])

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    print("no connection...")