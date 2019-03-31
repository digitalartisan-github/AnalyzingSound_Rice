import wave
from scipy import fromstring, int16
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

wavfile = '../assets/WashingRice_mono.wav'
# wavfile = 'ohayo.wav'
wr = wave.open(wavfile, "rb")
ch = wr.getnchannels()
width = wr.getsampwidth()
fr = wr.getframerate()
fn = wr.getnframes()

nperseg = 64 #256 #4096 #2048 #1024 #256 #128 #32 #64 #512

print('ch :', ch)
print('frame :', fn)
fs = fn / fr
print('fr :',fr)
print('sampling fs :', fs, 'sec')
print('width :', width)
origin = wr.readframes(wr.getnframes())
data = origin[:fn]
wr.close()
amp = max(data)
print('amp :',amp)

print('len of origin :', len(origin))
print('len of sampling: ', len(data))

# ステレオ前提 > monoral
x = np.frombuffer(data, dtype="int16")  #/32768.0
print('max(x):', max(x))
t = np.linspace(0, fs, fn/2, endpoint=False)
plt.title('Amp')
plt.plot(t, x)
plt.show()


f, t, Zxx = signal.stft(x, fs=fs*fn/20, nperseg=nperseg)

# plot
plt.figure()
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp)
# plt.xlim(0, fs)
plt.xlim(0, 0.1) # 0-0.07 sec までしか解析されない
plt.ylim([f[1], f[-1]])
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.yscale('log')
plt.show()


"""
https://qiita.com/MuAuan/items/858aab2879708668e2bb#stft%E5%A4%89%E6%8F%9B%E9%80%86%E5%A4%89%E6%8F%9B%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B%E9%81%A9%E5%BD%93%E3%81%AA%E7%AA%93%E9%96%A2%E6%95%B0%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E5%AE%9F%E8%A1%8C%E3%81%97%E3%81%A6%E3%81%BF%E3%81%BE%E3%81%97%E3%81%9F
"""