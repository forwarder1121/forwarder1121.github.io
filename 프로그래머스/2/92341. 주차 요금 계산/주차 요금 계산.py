import math
from collections import defaultdict
def solution(fees, records):
    
    def str2minute(time_stamp):
        HH,MM=map(int,time_stamp.split(":"))
        return HH*60+MM
    
    
    # COLLECTION
    car_infos=defaultdict(lambda: defaultdict(int))
    
    for record in records:
        time_stamp,car_number,content=record.split(" ")
        cur_time=str2minute(time_stamp)
        if content=="IN":
            car_infos[car_number]["IN"]=cur_time
            car_infos[car_number]["OUT"]=None
        elif content=="OUT":
            car_infos[car_number]["OUT"]=cur_time
            parking_minutes=car_infos[car_number]["OUT"]-car_infos[car_number]["IN"]
            car_infos[car_number]["TOTAL"]+=parking_minutes
            
    
    for car_number in car_infos:
        if not car_infos[car_number]["OUT"]:
            car_infos[car_number]["TOTAL"]+=str2minute("23:59")-car_infos[car_number]["IN"]
            
    
    print(car_infos)
    # CALCULATE
    base_time,base_fee,unit_time,unit_fee=fees
    results=[] # (number, fee)
    for car_number in car_infos:
        total_time=car_infos[car_number]["TOTAL"]
        if total_time<=base_time:
            results.append((car_number,base_fee))
        else:
            results.append((car_number,base_fee+math.ceil((total_time-base_time)/unit_time)*unit_fee))
    
    results.sort(key=lambda x:x[0])
    answer=[result[1] for result in results]
            
    
    return answer