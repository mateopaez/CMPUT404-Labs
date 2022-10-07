# The majority of the code comes from the multi_echo_server.py that was shown in the lab demo

#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #allow reused addresses
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        while True:
            # Accept connections and start a Process daemon for handling mutliple connections
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started process ", p)
            
def handle_echo(addr, conn):
    print("Connected by", addr)
    #recieve data, wait a bit, then send it back:
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()
