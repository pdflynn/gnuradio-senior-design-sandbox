import sys
import pmt
import zmq
import time

# Create PUSH socket
_PROTOCOL = "tcp://"
_SERVER = "127.0.0.1"  # localhost
_PUSH_PORT = ":50252"  # port
_PUSH_ADDR = _PROTOCOL + _SERVER + _PUSH_PORT

push_context = zmq.Context()
push_sock = push_context.socket(zmq.PUSH)
rc = push_sock.bind(_PUSH_ADDR)

# Create 13-bit Barker code preamble
BARKER_13 = "0001111100110101"
PREAMBLE = b"\x49\xA7\xB8\x7F\x1D\x8A\x5F\x54\x2D\xE7\x2B\x30\x6D\x74\x64\x40"


# Send data in a loop
with open("transmit_msg.txt", "rb") as f:
    MESSAGE = f.read()

while True:
    # push_sock.send(pmt.serialize_str(pmt.to_pmt(MESSAGE)))
    push_sock.send(PREAMBLE + MESSAGE)
    print("Sent message", PREAMBLE + MESSAGE)
    time.sleep(5)
