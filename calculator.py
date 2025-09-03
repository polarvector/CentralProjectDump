import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

# Constants
location = 'kathmandu'
T = 23
mic_distance_initial = 0.0072  # Distance between microphones in meters (7 mm)
sampling_rate = 48000  # Sampling rate in Hz
speed_of_sound = 331.3 + 0.6 * T  # Speed of sound in m/s
duration = 1e-3  # Duration of simulation (1 ms)

# Adjustable frequencies
low_frequency = 1000   # 1 kHz (low frequency case)
high_frequency = 20000 # 20 kHz (high frequency case)

# Precompute wavelength for both frequencies
wavelength_low = speed_of_sound / low_frequency
wavelength_high = speed_of_sound / high_frequency

# Time array for continuous simulation, sampling at 10x actual rate for "continuous" signal
high_sampling_rate = sampling_rate * 20  # 480 kHz
t_continuous = np.arange(0, duration, 1 / high_sampling_rate)

# Precompute the continuous wave for both frequencies
wave_mic1_low = np.sin(2 * np.pi * low_frequency * t_continuous)
wave_mic1_high = np.sin(2 * np.pi * high_frequency * t_continuous)

# Sampling indices for 48 kHz sampling rate
sample_indices = np.arange(0, len(t_continuous), int(high_sampling_rate / sampling_rate))
sampled_time = t_continuous[sample_indices]

# Set up plotting parameters (limits)
xlimit = [0, 0.5]
ylimit = [-2, 2]

for i in range(20):
    mic_distance = mic_distance_initial * (0.25*i + 1)
    time_delay_low = mic_distance / speed_of_sound
    time_delay_high = mic_distance / speed_of_sound

    # Simulate delayed waves at Mic 2
    wave_mic2_low = np.sin(2 * np.pi * low_frequency * (t_continuous - time_delay_low))
    wave_mic2_high = np.sin(2 * np.pi * high_frequency * (t_continuous - time_delay_high))

    # Sampled signals for both frequencies
    sampled_mic1_low = wave_mic1_low[sample_indices]
    sampled_mic2_low = wave_mic2_low[sample_indices]
    sampled_mic1_high = wave_mic1_high[sample_indices]
    sampled_mic2_high = wave_mic2_high[sample_indices]

    # Plotting (keep it efficient)
    plt.figure(figsize=(12, 10))

    # Low Frequency Plots
    plt.subplot(3, 2, 1)
    plt.plot(t_continuous * 1e3, wave_mic1_low, label='Mic 1 (Continuous)')
    plt.plot(t_continuous * 1e3, wave_mic2_low, label='Mic 2 (Continuous)', linestyle='--')
    plt.title(f'Low Frequency: 1 kHz (Wavelength: {wavelength_low:.2f} mm)')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 2, 2)
    plt.plot(sampled_time * 1e3, sampled_mic1_low, 'bo-', label='Mic 1 (Sampled)')
    plt.plot(sampled_time * 1e3, sampled_mic2_low, 'ro-', label='Mic 2 (Sampled)', linestyle='--')
    plt.title(f'Sampled at 48 kHz - Low Frequency ({low_frequency} Hz)')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    # High Frequency Plots
    plt.subplot(3, 2, 3)
    plt.plot(t_continuous * 1e3, wave_mic1_high, label='Mic 1 (Continuous)')
    plt.plot(t_continuous * 1e3, wave_mic2_high, label='Mic 2 (Continuous)', linestyle='--')
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(f'High Frequency: 20 kHz (Wavelength: {wavelength_high:.2f} mm)')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 2, 4)
    plt.stem(sampled_time * 1e3, sampled_mic1_high, 'bo-', label='Mic 1 (Sampled)')
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(f'Sampled at 48 kHz - High Frequency ({high_frequency} Hz)')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')

    plt.subplot(3, 2, 6)
    plt.stem(sampled_time * 1e3, sampled_mic2_high, 'ro-', label='Mic 2 (Sampled)')
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(f'Mic Distance: {mic_distance*1000:.2f} mm')

    # Correlation Plot
    idx = len(sampled_mic1_high)
    corr = correlate(sampled_mic1_high, sampled_mic2_high, mode='full')
    xx = np.arange(1 - idx, idx)
    plt.subplot(3, 2, 5)
    plt.title('Correlation of mic signals for high freq.')
    plt.plot(xx, corr)
    print(xx[np.argmax(corr)])

    plt.grid(True)
    plt.tight_layout()

    # Save plot (defer saving if possible to reduce I/O overhead)
    plt.savefig(f'scenarios//{location}//{T}_C_mics_dist_{i}.png')

