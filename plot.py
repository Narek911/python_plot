#! /usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    secondary_signal = []
    Fs = 1000                               # No. of samples per second (sample rate)
    F_1 = 1                                 # No. of cycles per second (the low frequency signal)
    F_2 = 100                               # No. of cycles per second (the high frequency signal)
    step = 1200                             # the length of 0 region
    length = 165                            # the length of high frequency region
    offset = 250                            # offset from the beginning
    sample = 8192                           # No. of samples to plot

    cycle_len = int(sample / 6)

    x = np.arange(sample)
    primary_signal = np.sin(2 * np.pi * F_1 * x / Fs)
    high_freq = np.sin(2 * np.pi * F_2 * x / Fs)

    data_0 = [0] * step
    secondary_signal.extend(data_0[0:offset])
    sample = sample - offset

    while sample:
        secondary_signal.extend(high_freq[0:length])
        secondary_signal.extend(data_0)
        sample = sample - cycle_len
        if sample < cycle_len:
            secondary_signal.extend(high_freq[0:length])
            secondary_signal.extend(data_0[0:sample - length])
            break

    z = primary_signal + secondary_signal
    plt.plot(x, z * 10000)
    plt.xlabel('sample(n)')
    plt.ylabel('Amplitude (v)')
    plt.show()


