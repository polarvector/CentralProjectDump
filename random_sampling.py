import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Function to generate a real-life-like signal
def generate_signal(duration_sec, sampling_rate=1000):
    t = np.linspace(0, duration_sec, int(sampling_rate * duration_sec))
    # Real-life-like signal: Combination of sinusoidal and random noise
    signal = (np.sin(2 * np.pi * 0.5 * t) + 0.5 * np.sin(2 * np.pi * 1.5 * t) +
              0.2 * np.sin(2 * np.pi * 3.5 * t) + np.random.normal(0, 0.1, t.shape))
    return t, signal

# Function to create an ill-behaved sampled signal
def sample_signal_random(t, signal, min_period, max_period):
    sampled_times = [t[0]]
    while sampled_times[-1] < t[-1]:
        sampled_times.append(sampled_times[-1] + np.random.uniform(min_period, max_period))
    sampled_times = np.array(sampled_times)
    sampled_signal = np.interp(sampled_times, t, signal)
    return sampled_signal

# Function to plot time-domain signal and frequency response
def plot_signals_and_responses(signals, sampling_rates):
    fig, axes = plt.subplots(len(signals), 2, figsize=(12, 24))
    titles = ['Original Signal (s1)', 'Ill-behaved Sampling [0.01, 0.02] (s2)',
              'Ill-behaved Sampling [0.01, 0.03] (s3)', 'Ill-behaved Sampling [0.01, 0.04] (s4)',
              'Ill-behaved Sampling [0.01, 0.05] (s5)', 'Ill-behaved Sampling [0.01, 0.06] (s6)',
              'Ill-behaved Sampling [0.01, 0.07] (s7)', 'Ill-behaved Sampling [0.01, 0.08] (s8)']
    
    for i, (signal, sr) in enumerate(zip(signals, sampling_rates)):
        t = np.linspace(0, len(signal) / sr, len(signal))
        # Plot the time-domain signal
        axes[i, 0].plot(t, signal)
        axes[i, 0].set_xlim([0, 10])
        axes[i, 0].set_ylim([-1.5, 1.5])
        axes[i, 0].set_title(f'{titles[i]} in Time Domain [s]', fontsize=10, pad=10)
        axes[i, 0].set_ylabel('Amplitude', fontsize=8)

        # Plot the frequency response
        N = len(signal)
        yf = fft(signal)
        xf = fftfreq(N, 1 / sr)[:N//2]
        axes[i, 1].plot(xf, 2.0/N * np.abs(yf[:N//2]))
        axes[i, 1].set_xlim([0, 5])
        axes[i, 1].set_ylim([0, 1])
        axes[i, 1].set_title(f'{titles[i]} Frequency Response [Hz]', fontsize=10, pad=10)
        axes[i, 1].set_ylabel('Magnitude', fontsize=8)
    
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.05, top=0.95, wspace=0.3, hspace=0.6)
    plt.show()

# Parameters
duration_sec = 1000  # seconds
sampling_rate = 1000  # samples per second

# Generate s1
t1, s1 = generate_signal(duration_sec, sampling_rate)

# Generate ill-behaved sampled signals with varying period limits
period_limits = [
    (0.01, 0.02), 
    (0.02, 0.03), 
    (0.03, 0.04), 
    (0.04, 0.05), 
    (0.05, 0.06), 
    (0.06, 0.07), 
    (0.07, 0.08)
]

sampled_signals = [s1]
effective_sampling_rates = [sampling_rate]

for min_period, max_period in period_limits:
    sampled_signal = sample_signal_random(t1, s1, min_period, max_period)
    sampled_signals.append(sampled_signal)
    effective_sampling_rate = 1 / np.mean(np.diff(np.linspace(0, duration_sec, len(sampled_signal))))
    effective_sampling_rates.append(effective_sampling_rate)

# Plotting the signals and their frequency responses
plot_signals_and_responses(sampled_signals, effective_sampling_rates)
