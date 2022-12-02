import cyberpi

from websocket_server import WebsocketServer
from datetime import datetime

def new_client(client, server):
    server.send_message_to_all(datetime.now().isoformat() + ": new client joined!")
    cyberpi.console.print("connected!\n")

    return

def on_message(client, server,message):
    cyberpi.console.print(message+"\n")
    print(message)
    if(message == "forward"):
        cyberpi.mbot2.EM_set_speed(10,"em1")
        cyberpi.mbot2.EM_set_speed(-10,"em2")
    elif(message=="backward"):
        cyberpi.mbot2.EM_set_speed(-10,"em1")
        cyberpi.mbot2.EM_set_speed(10,"em2")        
    elif(message=="stop"):
        cyberpi.mbot2.EM_set_speed(0,"all")

    distance = cyberpi.ultrasonic2.get()
    print(distance)
    server.send_message(client,str(distance))
    return

server = WebsocketServer("localhost",9999)
server.set_fn_new_client(new_client)
server.set_fn_message_received(on_message)
server.run_forever()
