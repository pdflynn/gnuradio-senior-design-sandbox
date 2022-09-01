import socket
import time

IP = "127.0.0.1"
PORT = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

BARKER_13 = b"7989"
asdf = b"1111100110101"
with open("transmit_msg.txt", "rb") as f:
    # message = str.encode("Greetings!")
    message = f.read()


try:
    sock.sendto(message, (IP, PORT))
    print("sent message")
    time.sleep(0.1)
except Exception as e:
    print(e)
    print("error!")
    sock.close()
# finally:
#     print("closing socket")
#     sock.close()
#     time.sleep(1)
