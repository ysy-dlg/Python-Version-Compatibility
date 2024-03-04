from scipy.signal import welch
from numpy.fft import fftshift, fft
from numpy import arange, exp, pi, mean
import matplotlib.pyplot as plt
#generate a 1000 Hz complex tone singnal
sample_rate = 48000. #sample rate must be a float
t=arange(1024*1024)/sample_rate
signal=exp(1j*2000*pi*t)
#amplitude correction factor
corr=1.5
#calculate the psd with welch
sample_freq, power = welch(signal, fs=sample_rate, window="hann", nperseg=256, noverlap=128, scaling='spectrum')
#fftshift the output 
sample_freq=fftshift(sample_freq)
power=fftshift(power)/corr
#check that the power sum is right
print sum(power)
plt.figure(figsize=(9.84, 3.94))
plt.plot(sample_freq, power)
plt.xlabel("Frequency (MHz)")
plt.ylabel("Relative power (dB)")  
plt.show()