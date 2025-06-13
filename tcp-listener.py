# ! ! CREATED BY CHATGPT FOR THIS PROJECT ! !
import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345      # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on port {PORT}... Press Ctrl+C to stop.")

    conn, addr = s.accept()
    with conn:
        print(f"Connection from {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
