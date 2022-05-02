
# This is the main file for hosting local server and managing the socket connection
from http import client
from lzma import FORMAT_ALONE
import socket
import threading
from .person import Person

HEADER = 64
PORT = 5050
HOSTNAME = socket.gethostname()
print("Hostname: ", HOSTNAME)
# SERVER = socket.gethostbyname(socket.getfqdn())
SERVER = '192.168.142.53'
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
    # print(f"[NEW CONNECTION] {addr} connected.")

    # check id of the client
    connected = True
    
    while connected:
        
        # receive msg from client
        msg = conn.recv(HEADER).decode(FORMAT)
        msg = int(msg)
        print("[Received] ", msg)
        if assert_msg():
            strength = str(people_dict[msg].get_strength())
            conn.send(strength.encode(FORMAT))
            print("[Sent] ", strength)
            connected = False
        
        # print("msg_length: ", msg_length)
        # if msg_length:
        #     # process received message
        #     # Message format: ID:n
        #     msg = int(msg_length)
        #     # msg = conn.recv(msg_length).decode(FORMAT)
        #     print("msg: ", msg)
        #     if msg == DISCONNECT_MESSAGE:
        #         connected = False    
            
        #     elif assert_msg():
        #         # valid message
        #         # client_id = int(msg[0])
        #         strength = str(strengths_list[0])

        #         connected = False
                
    # print(f"[DISCONNECTION] {addr} disconnected")
    conn.close()

def server_start(participants):
    """
    run the server
    """
    print("[STARTING] server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    print(socket.gethostname())
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, participants))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")


def assert_msg():
    return True