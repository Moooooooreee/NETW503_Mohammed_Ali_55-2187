import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '127.0.0.1'  # Change this to the server's actual IP address
    server_port = 5605  # Change this to the desired port number

    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    print("Server started. Waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Client connected:", client_address)

        while True:
            message = client_socket.recv(1024).decode()

            if message == "CLOSE SOCKET":
                break

            response = message.upper()
            client_socket.send(response.encode())

        print("Client disconnected:", client_address)
        client_socket.close()


if __name__ == '__main__':
    start_server()