import time
from smbus2 import SMBus
import max30100

mx30 = max30100.MAX30100()

def average(lst):
    return sum(lst) / len(lst)

def get_maxvalues():
    counter=20
    hr_vals=[]
    sp_vals=[]
    while(counter !=0 ):
        mx30.reinit()
        mx30.set_mode(max30100.MODE_SPO2)
        mx30.read_sensor()
        hrval=mx30.ir
        spOval=mx30.red
        pubval1=max30100.convertval(mx30.red)
        pubval2=max30100.convertit(mx30.ir)
        if ((pubval1 > 30) and (pubval2 > 30)):
            sp_vals.append(pubval1)
            hr_vals.append(pubval2)
            
            print("Added "+ str(counter))
        time.sleep(0.25)
        if (len(sp_vals)!=0):
            counter=counter-1

    print(average(hr_vals))
    print(average(sp_vals))
    mx30.reset()
    

get_maxvalues()

        
