import socket
import threading

active_connections = 0
active_connections_lock = threading.Lock()  # Lock for accessing active_connections

def handle_client(client_socket, client_address):
    global active_connections

    with active_connections_lock:
        active_connections += 1
        print("Client connected:", client_address)
        print("Active connections:", active_connections)

    while True:
        message = client_socket.recv(1024).decode()

        if message == "CLOSE SOCKET":
            break

        response = message.upper()
        client_socket.send(response.encode())

    with active_connections_lock:
        active_connections -= 1
        print("Client disconnected:", client_address)
        print("Active connections:", active_connections)

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '127.0.0.1'  # Change this to the server's actual IP address
    server_port = 5607  # Change this to the desired port number

    server_socket.bind((server_host, server_port))
    server_socket.listen(5)  # Increased backlog to allow multiple connections
    print("Server started. Waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()

        # Create a new thread and assign it to the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == '__main__':
    start_server()