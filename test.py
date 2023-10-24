import cyberpi
import math
import time
prev_time=time.time()*1000
while(1):
    a=10
    b=10
    cyberpi.mesh_broadcast.set("message", (((a + 100)) * 201 + ((b + 100))))
    mes = cyberpi.mesh_broadcast.get("message")
    c= math.floor(mes / 360)
    d=(mes%360)
    cur_time=time.time()*1000
    freq=1000/(cur_time-prev_time)
    prev_time=cur_time
    print(str(freq)+"Hz")
    print("c="+str(c)+" d="+str(d)+" "+str(freq)+"Hz")
