
# This is the main file for hosting local server and managing the socket connection
import socket

s = socket.socket()

s.bind(('0.0.0.0', 8090))
s.listen(0)

while True:

<<<<<<< Updated upstream
    client, addr = s.accept()
=======
# option 1: client asking server, and server responding
# Option 2: Server talking to client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
>>>>>>> Stashed changes

    while True:
        content = client.recv(32)


<<<<<<< Updated upstream
        if len(content) == 0:
            break
=======
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
>>>>>>> Stashed changes

        else:
            print(content)

    print("Closing connection")
    client.close()