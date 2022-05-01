
# This is the main file for hosting local server and managing the socket connection
from http import client
from lzma import FORMAT_ALONE
import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


# option 1: client asking server, and server responding
# Option 2: Server talking to client
def handle_client(conn, addr, strengths_list):
    print(f"[NEW CONNECTION] {addr} connected.")

    # check id of the client
    connected = True
    
    while connected:
        
        # receive msg from client
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            # process received message
            # Message format: ID:n
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False    
            
            elif assert_msg():
                # valid message
                client_id = int(msg[-1])
                strength = str(strengths_list[client_id])

                conn.send(strength.encode(FORMAT))
                pass            
    print(f"[DISCONNECTION] {addr} disconnected")
    conn.close()

def server_start(strengths):
    """
    run the server
    """
    print("[STARTING] server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, strengths))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")


def assert_msg():
    return True