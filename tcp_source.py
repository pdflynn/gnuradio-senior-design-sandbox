import socket
import time

IP = "127.0.0.1"
PORT = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

BARKER_13 = b"7989"
asdf = b"1111100110101"
messages = list()
with open("LONG_transmit_msg.txt", "rb") as f:
    # message = str.encode("Greetings!")
    messages = f.readlines()
    # while True:
    #     chunk = f.read(8) # read 8 bytes
    #     messages.append(chunk)
    #     if not chunk:
    #         break

# while True:
try:
    for message in messages:
        print("Sending", message)
        sock.sendto(message, (IP, PORT))
        time.sleep(0.0001)
    sock.sendto(str.encode(" "), (IP, PORT)) # for some reason the last packet gets "stuck"

except Exception as e:
    print(e)
    print("error!")
    sock.close()
finally:
    print("closing socket")
    sock.close()
    time.sleep(1)
