import socket
import time

IP = "127.0.0.1"
PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
print(f"Buffer size before: {bufsize}")
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1472)
bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
print(f"Buffer size after: {bufsize}")

BARKER_13 = b"7989"
asdf = b"1111100110101"
message = str.encode("Greetings!")


while True:
    try:
        sock.sendto(message, (IP, PORT))
        print("sent message")
    except Exception as e:
        print(e)
        print("error!")
    finally:
        # print("closing socket")
        # sock.close()
        time.sleep(1)