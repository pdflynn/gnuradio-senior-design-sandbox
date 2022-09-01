import socket
import time

IP = "127.0.0.1"
PORT = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((IP, PORT))
sock.listen(1)

(client, addr) = sock.accept()
print("connected to", client, addr)
while True:
    data = client.recv(1000)
    if not data: break
    print(data)
    with open("received.txt", "wb") as f:
        f.write(data)