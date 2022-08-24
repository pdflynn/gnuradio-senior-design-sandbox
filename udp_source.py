import socket
import time

TCP_IP = "127.0.0.1"
TCP_PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

BARKER_13 = b"7989"
asdf = b"1111100110101"
message = BARKER_13 + str.encode("Greetings!", encoding="UTF-8")

print(type(BARKER_13))
print(type(message))
package = message
print(package)

while True:
    try:
        sock.sendto(package, (TCP_IP, TCP_PORT))

        print("sent message")
        time.sleep(2)  # only send once a second to avoid overloading
    except:
        print("error!")
        sock.close()
        time.sleep(1)
