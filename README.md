# RTOS-Based Task Scheduler Simulation for Wearable Health Monitoring System

## 📌 Project Overview
This project simulates a wearable health monitoring system using a real-time task scheduler (RTOS concept) in Python. It includes synthetic ECG and PPG signals, digital signal processing (DSP) filtering, and priority-based task management without using any microcontroller or hardware.

## 🧱 Project Structure

- `data/`: Contains simulated ECG and PPG signal data
- `generate_signals.py`: Script to generate synthetic signals
- `dsp_filter.py`: Implements FIR low-pass and Butterworth band-pass filters
- `rtos_scheduler.py`: RTOS-style round-robin scheduler for tasks
- `task_heart_rate.py`: Calculates heart rate from ECG signal
- `task_oxygen_level.py`: Calculates SpO2 from PPG signal

## 🧠 Features
- RTOS-like multithreaded scheduler using Python
- Simulated biosignals
- Signal filtering using FIR and Butterworth filters
- Health parameter calculation

## ▶️ How to Run
1. Run `generate_signals.py` to generate ECG and PPG signals
2. Execute `rtos_scheduler.py` to simulate RTOS task management
3. Filtered outputs are printed to console and can be visualized via notebook

## 📈 Output
- Filtered signals
- Simulated heart rate and oxygen level
