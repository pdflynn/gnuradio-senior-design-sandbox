# %%
import socket

BARKER_13 = b"1111100110101"
UDP_IP = "127.0.0.1"
UDP_PORT = 9999


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(5)
sock.bind(('', UDP_PORT))

while True:
    try:
        data, addr = sock.recvfrom(1472)
        print('Received Data', data)

        with open("output_20220823.txt", "a") as f:
            # f.write(binary)
            pass

        # print(data)
    except socket.timeout:
        print('timeout')
        pass
# %%
