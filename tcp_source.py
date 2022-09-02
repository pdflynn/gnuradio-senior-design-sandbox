import socket
import time

IP = "127.0.0.1"
PORT = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

filename = "LONG_transmit_msg.txt"

messages = list()
with open(filename, "rb") as f:
    # message = str.encode("Greetings!")
    # messages = f.readlines()
    while True:
        chunk = f.read(16) # read 8 bytes
        messages.append(chunk)
        if not chunk:
            break

# while True:
try:
    for message in messages:
        print("Sending", message)
        sock.sendto(message, (IP, PORT))
        time.sleep(.10)
    sock.sendto(str.encode(" "), (IP, PORT))

except Exception as e:
    print(e)
    print("error!")
    sock.close()
finally:
    print("closing socket")
    sock.close()
    time.sleep(1)
