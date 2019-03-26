from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pyplot


# fft
# 逆fft

x = np.arange(5)
y = fft(x)
xy = ifft(y)

print("x :", x)
print("y :", y)
print("xy : ", xy)


"""
x : [0 1 2 3 4]
y : [10. +0.j -2.5+3.4409548j -2.5+0.81229924j -2.5-0.81229924j -2.5-3.4409548j]
xy :  [0.+0.j 1.+0.j 2.+0.j 3.+0.j 4.+0.j]
"""