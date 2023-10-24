import cyberpi
from makeblock.comm import SerialPort
import serial.tools.list_ports
import time
prev_time=time.time()*1000
cyberpi.goto_offline_mode()
while(1):
    enc1 = cyberpi.mbot2.EM_get_angle("em1")
    enc2 = cyberpi.mbot2.EM_get_angle("em2")
    power1=0.2*(90-enc1)
    power2=0.2*(90-enc2)
    cyberpi.mbot2.drive_power(power1,power2)
    cur_time=time.time()*1000
    freq=1000/(cur_time-prev_time)
    prev_time=cur_time
    print(str(freq)+"Hz")