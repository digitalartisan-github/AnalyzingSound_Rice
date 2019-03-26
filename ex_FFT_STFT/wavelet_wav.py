
from swan import pycwt
import numpy as np
import matplotlib.pyplot as plt
import wave
#import struct
from scipy import fromstring, int16
#from pylab import *
#from scipy import signal


wavfile = '../assets/WashingRice.wav'
#wavfile = 'ohayo.wav'
wr = wave.open(wavfile, "rb")
ch = wr.getnchannels()
width = wr.getsampwidth()
fr = wr.getframerate()
fn = wr.getnframes()
fs = fn / fr

print('ch', ch)
print('frame', fn)
print('fr',fr)
print('sampling fs ', fs, 'sec')
print('width', width)
origin = wr.readframes(wr.getnframes())
data = origin[:fn]
wr.close()
amp = max(data)
print(amp)

print('len of origin', len(origin))
print('len of sampling: ', len(data))

# ステレオ前提 > monoral
y = np.frombuffer(data, dtype="int16")  /32768.0
x = np.linspace(0,fs, fn/2, endpoint=False)
plt.plot(x, y)
plt.show()

Fs = 1/0.0001
omega0 = 5 #0.2 #1 #2 #8
# (1)　Freqを指定してcwt
freqs=np.arange(10,2000,2.5)
r=pycwt.cwt_f(y,freqs,Fs,pycwt.Morlet(omega0))
rr=np.abs(r)

plt.rcParams['figure.figsize'] = (10, 6)
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.75, 0.7, 0.2])
ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.60], sharex=ax1)
ax3 = fig.add_axes([0.83, 0.1, 0.03, 0.6])

ax1.plot(x, y, 'k')

img = ax2.imshow(np.flipud(rr), extent=[0, 3,10, 2000], aspect='auto')  #, interpolation='nearest')
twin_ax = ax2
twin_ax.set_yscale('log')
twin_ax.set_xlim(0, 3)
twin_ax.set_ylim(10, 2000)
ax2.tick_params(which='both', labelleft=False, left=False)
twin_ax.tick_params(which='both', labelleft=True, left=True, labelright=False)
fig.colorbar(img, cax=ax3)
plt.show()

plt.plot(freqs,rr)
plt.xscale('log')
plt.show()