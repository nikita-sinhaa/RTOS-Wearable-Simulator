
import numpy as np
from scipy.signal import butter, lfilter, firwin

def lowpass_filter(data, cutoff=5.0, fs=250, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b = firwin(order + 1, normal_cutoff)
    y = lfilter(b, 1.0, data)
    return y

def bandpass_filter(data, lowcut=0.5, highcut=5.0, fs=250, order=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y
