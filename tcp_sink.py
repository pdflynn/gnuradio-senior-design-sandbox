import socket
import time

IP = "127.0.0.1"
PORT = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.listen(1)

(client, addr) = sock.accept()
while True:
    data = client.recv(10000)
    binary = [str(d) for d in data]
    string = ""
    n = 0
    for _ in binary:
        string += _
        if n == 8:
            n = 0
            # string += " "
        n += 1
    if not data: break
    print(string)
    with open("received.txt", "w") as f:
        f.write(data)