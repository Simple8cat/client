from re import L
import socket
import threading
HEADER = 64
DISCONNECT_MSG = "exit"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR =(SERVER,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
def handle_client (conn , addr):
    print (f"[NEW CONNECTION]{ADDR} connected")
    connected = True
    while connected :
        if msg_len:
            msg_len = conn.recv(HEADER).decode('utf-8')
            msg_len = int (msg_len)
            msg = conn.recv(msg_len).decode('utf-8')
            if msg == DISCONNECT_MSG :
                connected = False
            print(f"[{addr}]{msg}")
    conn.close()


def start ():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True :
        conn , addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION]{threading.activeCount()-1}")
print("starting")
start()