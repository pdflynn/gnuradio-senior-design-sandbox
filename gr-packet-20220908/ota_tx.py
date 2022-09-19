#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Ota Tx
# GNU Radio version: 3.10.3.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import fec
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import pdu
from gnuradio import soapy
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
from packet_tx_danny import packet_tx_danny  # grc-generated hier_block



from gnuradio import qtgui

class ota_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ota Tx", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ota Tx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ota_tx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.Const_PLD = Const_PLD = digital.constellation_calcdist(digital.psk_4()[0], digital.psk_4()[1],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.Const_PLD.gen_soft_dec_lut(8)
        self.sps = sps = 4
        self.rep = rep = 3
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.nfilts = nfilts = 32
        self.k = k = 7
        self.hdr_format = hdr_format = digital.header_format_counter(digital.packet_utils.default_access_code, 3, Const_PLD.bits_per_symbol())
        self.eb = eb = 0.25
        self.unused_16QAM = unused_16QAM = digital.constellation_calcdist([(-3-3j), (-1-3j), (1-3j), (3-3j), (-3-1j), (-1-1j), (1-1j), (3-1j), (-3+1j), (-1+1j), (1+1j), (3+1j), (-3+3j), (-1+3j), (1+3j), (3+3j)], [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        16, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.unused_16QAM.gen_soft_dec_lut(8)
        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts,1.0, eb, (5*sps*nfilts))
        self.sdr_samp_rate = sdr_samp_rate = 2e6
        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps,1.0, eb, (11*sps*nfilts))
        self.gain_linear = gain_linear = 0.5
        self.freq_center = freq_center = 917e6
        self.enc_hdr = enc_hdr = fec.repetition_encoder_make(128, rep)
        self.enc = enc = fec.cc_encoder_make(8000,k, rate, polys, 0, fec.CC_TERMINATED, False)
        self.dum_enc = dum_enc = fec.dummy_encoder_make(2080)
        self.dum_dec = dum_dec = fec.dummy_decoder.make(2080)
        self.dec_hdr = dec_hdr = fec.repetition_decoder.make(hdr_format.header_nbits(),rep, 0.5)
        self.dec = dec = fec.cc_decoder.make(8000,k, rate, polys, 0, (-1), fec.CC_TERMINATED, False)
        self.bandwidth = bandwidth = 1e6
        self.Const_HDR = Const_HDR = digital.constellation_calcdist(digital.psk_2()[0], digital.psk_2()[1],
        2, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.Const_HDR.gen_soft_dec_lut(8)

        ##################################################
        # Blocks
        ##################################################
        self._gain_linear_range = Range(0.25, 10, 0.25, 0.5, 200)
        self._gain_linear_win = RangeWidget(self._gain_linear_range, self.set_gain_linear, "'gain_linear'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_linear_win)
        self.soapy_limesdr_sink_0 = None
        dev = 'driver=lime'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_limesdr_sink_0 = soapy.sink(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_limesdr_sink_0.set_sample_rate(0, sdr_samp_rate)
        self.soapy_limesdr_sink_0.set_bandwidth(0, bandwidth)
        self.soapy_limesdr_sink_0.set_frequency(0, freq_center)
        self.soapy_limesdr_sink_0.set_frequency_correction(0, 0)
        self.soapy_limesdr_sink_0.set_gain(0, min(max(40, -12.0), 64.0))
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            freq_center, #fc
            (bandwidth * 5), #bw
            "Transmitted FFT", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.05)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_window_normalized(False)

        self.qtgui_freq_sink_x_0_0_0.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0_0 = qtgui.const_sink_c(
            800, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0_0.enable_axis_labels(True)

        self.qtgui_const_sink_x_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_win)
        self.pdu_random_pdu_0 = pdu.random_pdu(10, 30, 0xFF, 2)
        self.packet_tx_danny_0 = packet_tx_danny(
            hdr_const=Const_HDR,
            hdr_enc=enc_hdr,
            hdr_format=hdr_format,
            pld_const=Const_PLD,
            pld_enc=dum_enc,
            psf_taps=tx_rrc_taps,
            sps=sps,
        )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(gain_linear)
        self.blocks_message_strobe_random_0 = blocks.message_strobe_random( pmt.cons(pmt.PMT_NIL, pmt.make_u8vector(256, 0x1F)), blocks.STROBE_UNIFORM, 100, 0)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_random_0, 'strobe'), (self.pdu_random_pdu_0, 'generate'))
        self.msg_connect((self.pdu_random_pdu_0, 'pdus'), (self.packet_tx_danny_0, 'in'))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.soapy_limesdr_sink_0, 0))
        self.connect((self.packet_tx_danny_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.packet_tx_danny_0, 0), (self.qtgui_const_sink_x_0_0_0_0, 0))
        self.connect((self.packet_tx_danny_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ota_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_Const_PLD(self):
        return self.Const_PLD

    def set_Const_PLD(self, Const_PLD):
        self.Const_PLD = Const_PLD
        self.packet_tx_danny_0.set_pld_const(self.Const_PLD)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rx_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.eb, (11*self.sps*self.nfilts)))
        self.set_tx_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, (5*self.sps*self.nfilts)))
        self.packet_tx_danny_0.set_sps(self.sps)

    def get_rep(self):
        return self.rep

    def set_rep(self, rep):
        self.rep = rep

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rx_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.eb, (11*self.sps*self.nfilts)))
        self.set_tx_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, (5*self.sps*self.nfilts)))

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format
        self.packet_tx_danny_0.set_hdr_format(self.hdr_format)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rx_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.eb, (11*self.sps*self.nfilts)))
        self.set_tx_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, (5*self.sps*self.nfilts)))

    def get_unused_16QAM(self):
        return self.unused_16QAM

    def set_unused_16QAM(self, unused_16QAM):
        self.unused_16QAM = unused_16QAM

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps
        self.packet_tx_danny_0.set_psf_taps(self.tx_rrc_taps)

    def get_sdr_samp_rate(self):
        return self.sdr_samp_rate

    def set_sdr_samp_rate(self, sdr_samp_rate):
        self.sdr_samp_rate = sdr_samp_rate
        self.soapy_limesdr_sink_0.set_sample_rate(0, self.sdr_samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps

    def get_gain_linear(self):
        return self.gain_linear

    def set_gain_linear(self, gain_linear):
        self.gain_linear = gain_linear
        self.blocks_multiply_const_vxx_0.set_k(self.gain_linear)

    def get_freq_center(self):
        return self.freq_center

    def set_freq_center(self, freq_center):
        self.freq_center = freq_center
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.freq_center, (self.bandwidth * 5))
        self.soapy_limesdr_sink_0.set_frequency(0, self.freq_center)

    def get_enc_hdr(self):
        return self.enc_hdr

    def set_enc_hdr(self, enc_hdr):
        self.enc_hdr = enc_hdr
        self.packet_tx_danny_0.set_hdr_enc(self.enc_hdr)

    def get_enc(self):
        return self.enc

    def set_enc(self, enc):
        self.enc = enc

    def get_dum_enc(self):
        return self.dum_enc

    def set_dum_enc(self, dum_enc):
        self.dum_enc = dum_enc
        self.packet_tx_danny_0.set_pld_enc(self.dum_enc)

    def get_dum_dec(self):
        return self.dum_dec

    def set_dum_dec(self, dum_dec):
        self.dum_dec = dum_dec

    def get_dec_hdr(self):
        return self.dec_hdr

    def set_dec_hdr(self, dec_hdr):
        self.dec_hdr = dec_hdr

    def get_dec(self):
        return self.dec

    def set_dec(self, dec):
        self.dec = dec

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.freq_center, (self.bandwidth * 5))
        self.soapy_limesdr_sink_0.set_bandwidth(0, self.bandwidth)

    def get_Const_HDR(self):
        return self.Const_HDR

    def set_Const_HDR(self, Const_HDR):
        self.Const_HDR = Const_HDR
        self.packet_tx_danny_0.set_hdr_const(self.Const_HDR)




def main(top_block_cls=ota_tx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
