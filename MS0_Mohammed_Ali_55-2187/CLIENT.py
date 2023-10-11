import socket

def start_client():
    server_host = '127.0.0.1'  # Change this to the server's actual IP address
    server_port = 5605  # Change this to the server's actual port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print("Connected to server.")

    while True:
        message = input("Enter a message (or 'CLOSE SOCKET' to exit): ")

        client_socket.send(message.encode())

        if message == "CLOSE SOCKET":
            break

        response = client_socket.recv(1024).decode()
        print("Server response:", response)

    print("Connection closed.")
    client_socket.close()


if __name__ == '__main__':
    start_client()