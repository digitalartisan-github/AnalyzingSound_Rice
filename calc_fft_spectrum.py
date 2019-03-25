import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import wave


def calc_fft(size):

    args = sys.argv
    wav_file = args[1]

    # opne wav file
    wf = wave.open(wav_file, "r")
    channels = wf.getnchannels()
    fr = wf.getnframes()

    # load wav
    chunk_size = fr
    amp = (2**8) ** wf.getsampwidth()/2

    data = wf.readframes(chunk_size)
    data = np.frombuffer(data, "int16")
    data = data/amp
    wave_v = data[::channels]

    hammingWindow = np.hamming(size)
    fr = 44100
    fr_30 = int(fr/30)
    d = 1.0 / fr
    freqList = np.fft.fftfreq(size, d)
    print("freqList :", freqList)


    for i in range(5532672):
    # for i in range(10000): # debug

        if (i%1470 == 0):

            frame_i = int(i/1470)
            num = "%05d" % frame_i

            FILE_t = "Spectrum - " + wav_file + ".wav - " + num
            FILE_out = "result/graph/" + num + ".png"

            windowedData = hammingWindow * wave_v[i:i+size]

            data_fft = np.fft.fft(windowedData)
            data_src = abs(data_fft*10)
            print(data_src)

            data_max = data_fft/max(abs(data_fft)) # 正規化？

            # plt.plot(freqList, abs(data_max))
            plt.plot(freqList, abs(data_src))
            # plt.bar(freqList, abs(data_src))


            plt.axis([0, 1000, 0, 100])

            plt.title(FILE_t)
            plt.xlabel("Frequency [Hz]"), plt.ylabel("Amblitude Spectrum")
            plt.show()
            plt.savefig(FILE_out)
            plt.clf()

            print(str(int(i/1470)))

    print("Finish!!")


calc_fft(1024)


"""
実行時に、wav のパスを渡す
ex
assets/WashingRice.wav

size ??
"""