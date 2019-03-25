import matplotlib.pyplot as plt
import numpy as np
import sys
import wave


def plot_amp():

    args = sys.argv
    wav_file = args[1]

    # open wav file
    wf = wave.open(wav_file, "r")

    channels = wf.getnchannels()
    fr = wf.getframerate()
    fn = wf.getnframes()
    time_sec = 1.0*fn/fr
    time = time_sec

    chunk_size = int(fr*time)
    amp = (2**8)**wf.getsampwidth()/2
    data_read = wf.readframes(chunk_size)
    data_src = np.frombuffer(data_read, "int16")
    data = data_src/amp


    # time axis
    size = float(chunk_size)
    x = np.arange(0, size/fr, 1/fr)



    # print("channel Count :", channels)
    ### out, 2
    ### Stereo



    """
    ### Multi Channels
    for i in range(channels):
        plt.plot(x, data[i::channels])
        # plt.plot(x, data[i::channels])

        print("i :", i)

        data_len = len(x)
        print("length :", data_len)
        ### out, 1323000
        ### 1323000 = 30 * 44100

        print("data", data)
        print("- - -")
    """


    ### Single Channel
    plt.plot(x, data[0::channels])

    data_len = len(x)
    print("length :", data_len)
    ### out, 1323000
    ### 1323000 = 30 * 44100

    print("data :", data)
    print("- - -")



    title = "Plot Amp - \"" + wav_file + "\""

    plt.title(title)
    plt.xlabel("Times [Sec]")
    plt.ylabel("Amplitude")
    plt.ylim([-1 , 1])
    # plt.ylim([-500, 500])

    plt.show()




plot_amp()

"""
実行時に、wav のパスを渡す
ex
assets/WashingRice.wav
"""