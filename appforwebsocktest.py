

from websocket_server import WebsocketServer
from datetime import datetime

import json

def new_client(client, server):
    sendmessage =datetime.now().isoformat() + ": new client joined!"
    server.send_message(client,sendmessage)
    print(sendmessage)
    return

def on_message(client, server,message):
    #cyberpi.console.print(message+"\n")
    #print("recv:" + message+"\n")
    recvdata = json.loads(message)
    #recvdata={}
    if("command" in recvdata):
        if(recvdata["command"] == "forward"):
            pass
        elif(recvdata["command"]=="backward"):
            pass
        elif(recvdata["command"]=="stop"):
            pass
        elif(recvdata["command"]=="reset"):
            pass
        elif(recvdata["command"]=="setpower"):
            if("power1" in recvdata):
                pass
            if("power2" in recvdata):
                pass
        elif(recvdata["command"]=="turn"):
            speed1 = 10
            speed2 = 10
            if("speed1" in recvdata):
                speed1=recvdata["speed1"]
            if("speed2" in recvdata):
                speed2=recvdata["speed2"]
            if("angle1" in recvdata):
                pass
            if("angle2" in recvdata):
                pass   

    distance = 100
    enc1 = datetime.now().second
    enc2 = 354
    stat = {
        "usdis":distance,
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
