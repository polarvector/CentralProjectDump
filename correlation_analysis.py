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

def simulate_autocorrelation_error(signal_length, window_sizes, num_trials, max_lag):
    errors = {w: [] for w in window_sizes}
    true_signal = np.random.randn(signal_length)
    
    for _ in range(num_trials):
        noise_signal = true_signal + np.random.randn(signal_length) * 0.1  # Adding some noise
        for w in window_sizes:
            num_windows = signal_length // w
            for i in range(num_windows):
                x = true_signal[i*w:(i+1)*w]
                y = noise_signal[i*w:(i+1)*w]
                corr = cross_correlation(x, y, max_lag)
                errors[w].append(np.var(corr))  # Measure variance as error metric
    
    return errors

# Parameters
signal_length = 44100  # 1 second of data at 44.1 kHz
window_sizes = [256, 512, 1024, 2048, 4096, 4096*16]
num_trials = 100  # Number of trials to average error
max_lag = 50  # Maximum lag

# Simulate errors
errors = simulate_autocorrelation_error(signal_length, window_sizes, num_trials, max_lag)

# Plotting
avg_errors = {w: np.mean(errors[w]) for w in window_sizes}
plt.figure()
plt.plot(window_sizes, [avg_errors[w] for w in window_sizes], marker='o')
plt.xlabel('Window Size')
plt.ylabel('Variance of Autocorrelation Estimate')
plt.title('Error in Autocorrelation vs. Window Size')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
