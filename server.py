import socket

def start_server(port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', int(port)))
    server_socket.listen(1)

    print(f"Listening on port {port}...")

    while True:
        conn, addr = server_socket.accept()
        request = conn.recv(1024).decode()

        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        conn.send(response.encode())
        conn.close()

if __name__ == '__main__':
    # Accept arguments from the command line
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=80)
    args = parser.parse_args()

    # Start the server
    start_server(args.port)

