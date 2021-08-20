import scipy
import numpy
import matplotlib.pyplot as plt
from polyphase import Channelizer

channel_num = 8
# Sampling rate set to 1KHz
fs = 1000

f0 = 80
f1 = 100
t1 = 1


# 
T = 1

t = numpy.arange(0, int(T*fs)) / fs

s = scipy.signal.chirp(t, f0, t1, f1)

# 
cutoff = fs / channel_num / 2    # Desired cutoff frequency, Hz
trans_width = cutoff / 10  # Width of transition from pass band to stop band, Hz
numtaps = 128      # Size of the FIR filter.
taps = scipy.signal.remez(numtaps, [0, cutoff - trans_width, cutoff + trans_width, 0.5*fs],
                    [1, 0], Hz=fs)
    
channelizer = Channelizer(taps, channel_num)

ss = channelizer.dispatch(s)

plt.subplot(311)
plt.plot(numpy.real(s))
plt.subplot(312)
plt.plot(numpy.real(ss[0:4].T))
plt.subplot(313)
plt.plot(numpy.imag(ss[0:4].T))

plt.show()












