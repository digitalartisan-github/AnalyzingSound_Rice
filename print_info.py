import sys
import struct
from scipy import fromstring, int16
import wave


def print_info():

    args = sys.argv
    wav_file  = args[1]
    # print(wav_file)
    wave_r = wave.open(wav_file, "r")

    # get info
    ch = wave_r.getnchannels()
    width = wave_r.getsampwidth()
    fr = wave_r.getframerate()
    fn = wave_r.getnframes()
    time_sec = 1.0*fn/fr
    minites = int(time_sec // 60)
    seconds = time_sec % 60

    print("- - - - -")
    print("Channel :", ch)
    print("Width :", width)
    print("Frame Rate :", fr, "Hz")
    print("Frame num : ", fn)
    # print("Param :", wave_r.getparams())
    print("Total Time :", minites, "min", seconds, "sec")
    print("Tatal Time(sec) :", time_sec, "sec")
    print("- - - - -")

    #data = wave_r.readframes(wave_r.getnframes())
    wave_r.close()
    #X = fromstring(data, dtype=int16)


print_info()

"""
実行時に、wav のパスを渡す
ex
assets/WashingRice.wav
"""