import cyberpi

from websocket_server import WebsocketServer
from datetime import datetime

import json

def new_client(client, server):
    sendmessage =datetime.now().isoformat() + ": new client joined!"
    server.send_message(client,sendmessage)
    print(sendmessage)

    cyberpi.console.print("connected!\n")

    return

def on_message(client, server,message):
    #cyberpi.console.print(message+"\n")
    #print("recv:" + message+"\n")
    recvdata = json.loads(message)
    #recvdata={}
    if("command" in recvdata):
        if(recvdata["command"] == "forward"):
            cyberpi.mbot2.EM_set_speed(10,"em1")
            cyberpi.mbot2.EM_set_speed(-10,"em2")
        elif(recvdata["command"]=="backward"):
            cyberpi.mbot2.EM_set_speed(-10,"em1")
            cyberpi.mbot2.EM_set_speed(10,"em2")        
        elif(recvdata["command"]=="stop"):
            cyberpi.mbot2.EM_stop("all")
        elif(recvdata["command"]=="reset"):
            cyberpi.mbot2.EM_reset_angle("all")
        elif(recvdata["command"]=="setpower"):
            # if("power1" in recvdata ):
            #     cyberpi.mbot2.EM_set_power(recvdata["power1"],"em1")
            # if("power2" in recvdata):
            #     cyberpi.mbot2.EM_set_power(recvdata["power2"],"em2")
            if(("power1" in recvdata ) & ("power1" in recvdata )):
                cyberpi.mbot2.drive_power(recvdata["power1"], recvdata["power2"])
        elif(recvdata["command"]=="turn"):
            speed1 = 10
            speed2 = 10
            if("speed1" in recvdata):
                speed1=recvdata["speed1"]
            if("speed2" in recvdata):
                speed2=recvdata["speed2"]
            if("angle1" in recvdata):
                cyberpi.mbot2.EM_turn(recvdata["angle1"],speed1,"em1")
            if("angle2" in recvdata):
                cyberpi.mbot2.EM_turn(recvdata["angle2"],speed2,"em2")   

    #distance = cyberpi.ultrasonic2.get()
    enc1 = cyberpi.mbot2.EM_get_angle("em1")
    enc2 = cyberpi.mbot2.EM_get_angle("em2")
    stat = {
        #"usdis":distance,
        "enc1":enc1,
        "enc2":enc2,
    }
    senddata= json.dumps(stat)
    #print(senddata)
    server.send_message(client,senddata)
    return

server = WebsocketServer("localhost",9999)
server.set_fn_new_client(new_client)
server.set_fn_message_received(on_message)
server.run_forever()
