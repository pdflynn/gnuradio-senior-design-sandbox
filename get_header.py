import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import pmt
from gnuradio import channels
from gnuradio import digital
from gnuradio import fec
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import pdu
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore

print(digital.packet_utils.default_access_code)
print(type(digital.packet_utils.default_access_code))
print(len(digital.packet_utils.default_access_code))

print(digital.header_format_counter(digital.packet_utils.default_access_code, 3, 2).header_nbits())