import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Number of experiments
n_experiments = 100
num_range  = 1000
max_counts = []

# Repeat the experiment n_experiments times
for exp_num in range(1, n_experiments + 1):
    match_counts = []    

    for target in range(1, num_range+1):
        count = 0
        while True:
            count += 1
            guess = random.randint(1, num_range)
            if guess == target:
                break
        match_counts.append(count)
        
    # Plot the result
    if (1==0):
        plt.figure(figsize=(12, 6))
        color = cm.viridis(exp_num / n_experiments)  # Unique color per experiment
        #plt.plot(range(1, num_range+1), np.argsort(match_counts), marker='.', linestyle='none', alpha=0.6, color=color)
        plt.plot(range(1, num_range+1),  np.sort(match_counts), marker='.', linestyle='none', alpha=0.6, color=color)
        print(max(match_counts))
        plt.title(f'Experiment {exp_num}: Iterations to Match Each Target')
        plt.xlabel('Target Number')
        plt.ylabel('Iterations to Match')
        plt.grid(True)
        plt.tight_layout()

        # Save the figure
        filename = f"{exp_num}.jpg"
        plt.savefig(filename)
        plt.close()  # Close the figure to free memory
    max_counts.append(max(match_counts))

plt.scatter(range(1,n_experiments+1), max_counts)
print(np.average(max_counts))
plt.show()
filename_list = [f"{i}.jpg" for i in range(1, n_experiments + 1)]
filename_list
