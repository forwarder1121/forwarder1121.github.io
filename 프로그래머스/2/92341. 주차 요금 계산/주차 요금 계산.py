from collections import defaultdict
import math
def solution(fees, records):
    reports=defaultdict(lambda : defaultdict(int))
    
    def time2minute(time_stamp):
        HH,MM=map(int,time_stamp.split(":"))
        return HH*60+MM
    
    for record in records:
        time_stamp, car_number, content=record.split(" ")
        minute=time2minute(time_stamp)
        if content=="IN":
            reports[car_number]["in_time"]=minute
            reports[car_number]["is_now_parked"]=True
        else:
            reports[car_number]["total_parked_time"]+=\
            minute-reports[car_number]["in_time"]
            reports[car_number]["is_now_parked"]=False
            
    for car_number in reports:
        if reports[car_number]["is_now_parked"]:
            reports[car_number]["total_parked_time"]+=\
            time2minute("23:59")-reports[car_number]["in_time"]
    
    bt, bf, ut, uf=fees
    
    def calculate_tax(tt):
        if tt<=bt:
            return bf
        else:
            return bf+math.ceil((tt-bt)/ut)*uf
    
    result=[]
    for car_number in reports:
        tax=calculate_tax(reports[car_number]["total_parked_time"])
        result.append((int(car_number),tax))
    result.sort()
    
    answer=[tax for _,tax in result]
    return answer