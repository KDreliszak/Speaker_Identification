# from __future__ import print_function, division, unicode_literals

import wave
import numpy as np


def noise_reduction(wave_file, filtered_file):
    wr = wave.open(wave_file, 'r')
    par = list(wr.getparams())  # Get the parameters from the input.
    par[3] = 0  # The secber of samples will be set by writeframes.

    # Open the output file
    ww = wave.open(filtered_file, 'w')
    ww.setparams(tuple(par))  # Use the same parameters as the input file.

    lowpass = 380  # Remove lower frequencies.
    highpass = 9000  # Remove higher frequencies.

    framreate = wr.getframerate()  # Read and process 1 second at a time.
    length = int(wr.getnframes()/framreate)  # whole file

    for sec in range(length):
        print('Processing {}/{} s'.format(sec+1, length))
        da = np.frombuffer(wr.readframes(framreate), dtype=np.int16)
        left, right = da[0::2], da[1::2]  # left and right channel
        lf, rf = np.fft.rfft(left), np.fft.rfft(right)
        lf[:lowpass], rf[:lowpass] = 0, 0  # low pass filter
        lf[55:66], rf[55:66] = 0, 0  # line noise
        lf[highpass:], rf[highpass:] = 0, 0  # high pass filter
        nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
        ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
        ww.writeframes(ns.tostring())

    # Close the files.
    wr.close()
    ww.close()


noise_reduction('test.wav', 'filtered-test.wav')

