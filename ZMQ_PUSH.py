import sys
import pmt
import zmq
import time
import keyboard

# Create PUSH socket
_PROTOCOL = "tcp://"
_SERVER = "127.0.0.1"  # localhost
_PUSH_PORT = ":50252"  # port
_PUSH_ADDR = _PROTOCOL + _SERVER + _PUSH_PORT

push_context = zmq.Context()
push_sock = push_context.socket(zmq.PUSH)
rc = push_sock.bind(_PUSH_ADDR)

# Create pseudorandom preamble
# BARKER_13 = "0001111100110101" # unused
PREAMBLE = b"\x49\xA7\xB8\x7F\x1D\x8A\x5F\x54\x2D\xE7\x2B\x30\x6D\x74\x64\x40"
# PREAMBLE = b"\x49\xA7\xB8\x7F\x1D\x8A\x5F\x54"

# Set data rate
R_b = 128 # currently 1.024 kbps

with open("transmit_msg.txt", "rb") as f:
    MESSAGE = f.read()

# # send data in loop
# while True:
#     print("Sending Message")
#     push_sock.send(PREAMBLE + MESSAGE)
#     count = 0
#     time.sleep(0.25)

bytes_to_send = list()
for b in PREAMBLE:
    bytes_to_send.append(b)
for b in MESSAGE:
    bytes_to_send.append(b)

while len(bytes_to_send) > 0:
    b = bytes_to_send.pop(0)
    push_sock.send_string(chr(b))

# c = 0
# while True:
#     if len(bytes_to_send) > 0 and c > 4:
#         b = bytes_to_send.pop(0)
#         push_sock.send_string(chr(b))
#         c = 0
#     else:
#         push_sock.send_string(chr(0))
#         c += 1
