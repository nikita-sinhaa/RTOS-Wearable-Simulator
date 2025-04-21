
import pandas as pd
from dsp_filter import bandpass_filter

def oxygen_level_task():
    data = pd.read_csv('data/ppg_signal.csv')
    filtered = bandpass_filter(data['PPG'])
    oxygen_level = 95 + (filtered[500] - filtered[1]) * 2  # Dummy calc
    print(f"Oxygen Level Task: Approx SpO2 = {int(oxygen_level)}%")
