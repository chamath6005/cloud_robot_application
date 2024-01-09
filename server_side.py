import socket
import ssl

HOST = 'localhost'
PORT = 12345

def start_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="certfile.pem", keyfile="privkey.pem")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        with context.wrap_socket(server_socket, server_side=True) as ssl_socket:
            print("Server started. Waiting for connections...")
            conn, addr = ssl_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                print(f"Received data: {data.decode()}")
                conn.sendall(b"Server received your message.")

if __name__ == "__main__":
    start_server()
