import datetime
import zmq
import pmt
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for a request and send back the system time
    msg = socket.recv()
    print("Received Request: %s" % msg)

    # To send to GNU Radio, we need to use pmt
    # This is the way the example did it...take a string,
    # convert it to "pmt" with to_pmt, and then use
    # serialize_str as the value to actually send.
    time_val = datetime.datetime.now().time()
    pmt_val = pmt.to_pmt(str(time_val))
    send_val = pmt.serialize_str(pmt_val)
    print("Sending: %s" % send_val)

    socket.send(send_val)

    time.sleep(.01)
