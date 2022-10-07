# The amjority of this code comes from the proxy_servy.py that was shown in the lab demo

#!/usr/bin/enb python3
import socket, time, sys

# Defining global address and buffer size:
HOST = " "
PORT = 8001
BUFFER_SIZE = 1024

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
    # Connecting to google:
    host = 'www.google.com'
    port = 80

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

                # Connect to proxy_end:
                proxy_end.connect((remote_ip, port))
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

            # Closing connecting:
            conn.close

if __name__ == '__main__':
    main()