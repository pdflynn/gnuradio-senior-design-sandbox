import sys
import pmt
import zmq
import time

_PROTOCOL = "tcp://"
_SERVER = "127.0.0.1"  # localhost
_PULL_PORT = ":50251"  # port
_PULL_ADDR = _PROTOCOL + _SERVER + _PULL_PORT

pull_context = zmq.Context()
pull_sock = pull_context.socket(zmq.PULL)
rc = pull_sock.connect(_PULL_ADDR)

with open(f"received_messages/{str(time.strftime('%H%M%S'))}_binary.txt", "w") as f:
    while True:
        data = pull_sock.recv()
        # print(data) # data is a byte string where each byte is a bit
        #             # gnuradio can only send bytes, not individual bits.
        for d in data:
            print(d)
            f.write(str(d))