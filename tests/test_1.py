import scipy
import matplotlib.pyplot as plt
from polyphase import Channelizer

# Design FIR Filter
channel_num = 8
cutoff = 1 / channel_num / 2    # Desired cutoff digital frequency
trans_width = cutoff / 10  # Width of transition from pass band to stop band
numtaps = 512      # Size of the FIR filter.
taps = scipy.signal.remez(numtaps, [0, cutoff - trans_width, cutoff + trans_width, 0.5],[1, 0])

channelizer = Channelizer(taps, channel_num)

w, a = channelizer.sweep_freqz()

plt.plot(w,a.T)
plt.title('Digital channelizer frequency response')
plt.xlabel('Frequency [*rad/sample]')
plt.ylabel('Amplitude [dB]')
plt.show()
pass
