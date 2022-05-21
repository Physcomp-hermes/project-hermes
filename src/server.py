
# This is the main file for hosting local server and managing the socket connection
from http import client
from lzma import FORMAT_ALONE
import socket
import threading
from .person import Person

# TODO: Send and receive more information
HEADER = 64
PORT = 5050
HOSTNAME = socket.gethostname()
print("Hostname: ", HOSTNAME)
# SERVER = socket.gethostbyname(socket.getfqdn())
SERVER = '10.0.0.3'
ADDR = (SERVER, PORT)
# TADDR = (TSERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(ADDR)
server.bind(ADDR)

# option 1: client asking server, and server responding
# Option 2: Server talking to client
def handle_client(conn, addr, people_dict):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    # check id of the client
    connected = True
    
    while connected:
        # check whether it's a request for colour or upate strength
        # Colour communication: C-[id]. 
        # Example: C-1 for colour of the first one
        # Vibration communicaiton: V-[id]
        # Example: V-2 for vibration of second device

        # receive msg from client
        msg = conn.recv(HEADER).decode(FORMAT).split("-")
        device_id = int(msg[1])
        if msg[0] == "C":
            # Send colour to the device
            # Colour is sent as a string.. for now
            if device_id in people_dict:
                color = str(people_dict[device_id].get_colour())
                conn.send(color.encode(FORMAT))
                print("[Sent] ", color)
            else:
                conn.send("0000".encode(FORMAT))
                print("Colour request for unregistered person")
                
        
        elif msg[0] == "V":

            if device_id in people_dict:
                strength = str(people_dict[device_id].get_strength())
                conn.send(strength.encode(FORMAT))
                print("[Sent] ", strength)
            else:
                conn.send("0".encode(FORMAT))
                print("colour request for unregistered person")
        else:
            print("Wrong communication")
        connected = False
        
    conn.close()

def server_start(participants):
    """
    run the server. Currently, the server starts a thread that handles the request from the client.
    """
    print("[STARTING] server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    print(socket.gethostname())
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, participants))
        thread.start()


def assert_msg():
    return True
