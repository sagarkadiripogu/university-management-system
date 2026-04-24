from datetime import datetime,time as dtime
import time
def check_valid_time():
    cdt = datetime.now()
    ct = cdt.time()
    st = dtime(8,0,0)
    et = dtime(22,0,0)
    if ct >= st and ct <= et:
        pass
    else:
        print()
        s="Out of Working Hours...."
        for i in s:
            print(i,end="")
            time.sleep(0.1)
        print()
        exit()
check_valid_time()
