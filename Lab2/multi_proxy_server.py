# Majority of this code comes from proxy_server.py and multi_echo_server.py as shown in the lab demo

#!/usr/bin/enb python3
import socket, time, sys
from multiprocessing import Process

# Defining global address and buffer size:
HOST = " "
PORT = 8001
BUFFER_SIZE = 1024

# For connection to google:
host = 'www.google.com'
port = 80

# Get IP:
def get_remote_ip(host):
    print(f"Getting IP for {host}")
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting...")
        sys.exit()

    print(f"IP address of {host} is {remote_ip}")
    return remote_ip

def main():

    # Creating socket:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print('Starting proxy server...')
        # Allowing reused address:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Binding to host and port:
        proxy_start.bind(HOST, PORT)
        # Set socket to listening mode:
        proxy_start.listen(1)

        while True:
            conn, addr = proxy_start.accept()
            print('Connected by', addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print('Connecting to Google...')
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip, port))

                p = Process(target=handle_proxy, args=(addr, conn))
                p.daemon = True
                p.start()
                print("Started process ", p)

            # Closing connecting:
            conn.close

def handle_proxy(conn, addr, proxy_end):
    # Sending data to server:
    recievedData = conn.recv(BUFFER_SIZE)
    print(f'Sending recieved data {recievedData} to Google...')
    proxy_end.sendall(data)
    # Shutting down proxy_end:
    proxy_end.shutdown(socket.SHUT_RDWR)

    # Sending data to client:
    data = proxy_end.revc(BUFFER_SIZE)
    print(f'Sending recieved data {data} to client...')
    conn.send(data)
    conn.close


if __name__ == '__main__':
    main()