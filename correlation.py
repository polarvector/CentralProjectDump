import numpy as np
import matplotlib.pyplot as plt

def cross_correlation(x, y, max_lag):
    N = len(x)
    correlation = np.zeros(2 * max_lag + 1)
    for lag in range(-max_lag, max_lag + 1):
        if lag < 0:
            correlation[lag + max_lag] = np.sum(x[:N+lag] * y[-lag:N])
        else:
            correlation[lag + max_lag] = np.sum(x[lag:N] * y[:N-lag])
    return correlation / N

# Example usage
fs = 44100  # Sampling frequency
window_size = 1024  # Size of the sliding window
max_lag = 50  # Maximum lag in samples

# Initialize buffers
buffer_x = np.zeros(window_size)
buffer_y = np.zeros(window_size)

# Initialize plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
lag_indices = np.arange(-max_lag, max_lag + 1)
line, = ax.plot(lag_indices, np.zeros(2 * max_lag + 1))
ax.set_ylim([-1, 1])
ax.set_xlim([-max_lag, max_lag])
ax.set_xlabel('Lag')
ax.set_ylabel('Correlation')
ax.set_title('Real-Time Cross-Correlation')

# In a real-time loop, update buffers with new samples and calculate cross-correlation
while True:
    # Simulate receiving new samples (in practice, replace with actual audio data)
    x_new = np.random.randn(window_size)
    y_new = np.random.randn(window_size)
    
    # Update buffers
    buffer_x = np.roll(buffer_x, -window_size)
    buffer_y = np.roll(buffer_y, -window_size)
    buffer_x[-window_size:] = x_new
    buffer_y[-window_size:] = y_new
    
    # Compute cross-correlation for the current window
    correlation = cross_correlation(buffer_x, buffer_y, max_lag)
    
    # Update plot
    line.set_ydata(correlation)
    plt.draw()
    plt.pause(0.01)  # Pause briefly to update the plot

    # Find the lag with the maximum correlation (time delay estimation)
    max_corr_index = np.argmax(correlation)
    lag = max_corr_index - max_lag
    
    # Print lag and correlation (or handle it as needed)
    print(f"Lag: {lag}, Correlation: {correlation[max_corr_index]}")

    # Add your real-time handling code here (e.g., further processing, plotting, etc.)
