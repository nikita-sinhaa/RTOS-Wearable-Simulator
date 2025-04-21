
import pandas as pd
from dsp_filter import lowpass_filter

def heart_rate_task():
    data = pd.read_csv('data/ecg_signal.csv')
    filtered = lowpass_filter(data['ECG'])
    heart_rate = 75 + (filtered[1000] - filtered[1]) * 5  # Dummy calc
    print(f"Heart Rate Task: Approx HR = {int(heart_rate)} bpm")
