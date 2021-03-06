# polyphase

## Introduction

Polyphase channelizer implement using Python.

## Install Instructions

This package can be installed via pip. Simply run:

```bash
pip install polyphase
```

## How to Use

Import the necessary packages.

```python
import numpy
import scipy
import matplotlib.pyplot as plt

from polyphase import Channelizer

channel_num = 8
```

Create a Chirp Signal

```python

# Sampling rate set to 1KHz
fs = 1000

f0 = 80
f1 = 100
t1 = 1

t = numpy.arange(0, int(t1*fs)) / fs

s = scipy.signal.chirp(t, f0, t1, f1)
```

Design Filter.

```python
# 
cutoff = fs / channel_num / 2    # Desired cutoff frequency, Hz
trans_width = cutoff / 10  # Width of transition from pass band to stop band, Hz
numtaps = 128      # Size of the FIR filter.
taps = scipy.signal.remez(numtaps, [0, cutoff - trans_width, cutoff + trans_width, 0.5*fs],
                    [1, 0], Hz=fs)
```

Create a channelizer, and process signal.

```python
channelizer = Channelizer(taps, channel_num)

ss = channelizer.dispatch(s)

plt.subplot(311)
plt.plot(numpy.real(s))
plt.subplot(312)
plt.plot(numpy.real(ss[0:4].T))
plt.subplot(313)
plt.plot(numpy.imag(ss[0:4].T))
plt.show()

```

You can also run [test_1.py](./tests/test_1.py) and [test_2.py](./tests/test_2.py) for test.
