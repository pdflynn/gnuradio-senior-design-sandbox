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

# Attempt to pull data
received = False
while not received:
    try:
        data = pull_sock.recv()  # Just grabs the data from gr output

        # Format the received bits into bytes
        # gr is using a byte for every bit because byte is the
        # smallest datatype it can work with.
        received_bits = ""
        curr_byte = ""
        message_bytes = list()
        count = 0
        for d in data:
            curr_bit = "{:0b}".format(d)
            received_bits += curr_bit
            curr_byte += curr_bit
            count += 1

            if count == 8:
                message_bytes.append(curr_byte)
                curr_byte = ""
                count = 0

        # Now, message_bytes contains each byte in the sequence.
        print("Message Bits:", message_bytes)

        # We now desire to convert the strings of bits into actual bytes
        # message_literals = list()
        # for bitstring in message_bytes:
        #     byte = int(bitstring, 2)
        #     message_literals.append(byte)
        # more Pythonic way to do above:
        message_literals = [int(bitstring, 2) for bitstring in message_bytes]
        print(message_literals)
        with open(f"received_messages/{str(time.strftime('%H%M%S'))}_message.txt", "wb") as f:
            for m in message_literals:
                f.write(m.to_bytes(1, "little"))
        with open(f"received_messages/{str(time.strftime('%H%M%S'))}_binary.txt", "w") as f:
            f.write(received_bits)

    except Exception as e:
        print(e)
        print("timeout")
        pass
