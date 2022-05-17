
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
SERVER = socket.gethostbyname(socket.getfqdn())
# SERVER = '192.168.142.53'
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
        
        # receive msg from client
        msg = conn.recv(HEADER).decode(FORMAT)
        msg = int(msg)
        if assert_msg():
            strength = str(people_dict[msg].get_strength())
            conn.send(strength.encode(FORMAT))
            print("[Sent] ", strength)
            # return color 
            # The colour is hard coded in the device. Just send the index to the device.
            color = str(people_dict[msg].get_color())
            conn.send(color.encode(FORMAT))
            print("[Sent] ", color)
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
        # print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")


def assert_msg():
    return True
