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


    # open wav
    wf = wave.open(wav_file, "r")
    channels = wf.getnchannels()
    fr = wf.getnframes()

    chunk_size = fr
    amp = (2**8) ** wf.getsampwidth()/2

    data = wf.readframes(chunk_size)
    data = np.frombuffer(data, "int16")
    data = data/amp
    wave_v = data[::channels]


    # ハミング窓関数
    # 波形を整える ?
    hammingWindow = np.hamming(size)

    fr = 44100
    fr_30 = int(fr/30)
    d = 1.0 / fr
    freqList = np.fft.fftfreq(size, d)
    print("freqList :", freqList)



    for i in range(5532672):
    # for i in range(50000): # for debug

        # Sampling 30fps (44100/30 = 1470)
        if (i%1470 == 0):

            frame_i = int(i/1470)
            num = "%05d" % frame_i

            FILE_t = "Spectrum - " + wav_file + ".wav - " + num
            FILE_out = "result/graph/" + num + ".png"

            # fft
            windowedData = hammingWindow * wave_v[i:i+size]
            data_fft = np.fft.fft(windowedData)

            # plot
            # *10 特に意味なし、値が小さすぎたので大きく
            data_fft_expansion = abs(data_fft*10)
            plt.plot(freqList, data_fft_expansion)
            print(data_fft_expansion)

            # 正規化 ?
            # data_max = data_fft/max(abs(data_fft))
            # plt.plot(freqList, abs(data_max))

            plt.axis([0, 4000, 0, 50])
            plt.title(FILE_t)
            plt.xlabel("Frequency [Hz]"), plt.ylabel("Amblitude Spectrum")
            plt.show()
            plt.savefig(FILE_out) # export matplot image
            plt.clf()

            print(str(int(i/1470)))

    print("Finish!!")



calc_fft(1024)


"""
実行時に、wav のパスを渡す
ex
assets/WashingRice.wav

clac_fft(size)
size : ハミング窓関数 による波形編集の度合い??
"""