# The majority of this code comes from the proxy_client.py that was shown in the lab demo

#!/usr/bin/env python3
import socket

# Defining global address and buffer size:
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    # Creating socket, connecting and recieving data:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_RDWR)

        recievedData = s.recv(BUFFER_SIZE)
        print(recievedData)

    except Exception as e:
        print(e)

    # Closing socket:
    finally:
        s.close

def main():
    connect('127.0.0.1', 8001)

if __name__ == '__main__':
    main()


