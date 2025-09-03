import numpy as np
import matplotlib.pyplot as plt

def collatz(num):
    def collatz_seq(myNum):
        number = myNum
        if number%2 == 0:
            return number//2
            
        elif number%2 != 0:
            return 3*number+1
        
    try:
        initialVal = num
    except ValueError:
        print('Enter an integer')
        exit()

    values = np.array([initialVal])

    while initialVal != 1:
        initialVal = collatz_seq(initialVal)
        values = np.append(values,initialVal)

    x = np.linspace(1, len(values), len(values))
    plt.plot(x, values, label=f'Initial Value: {num}')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title('Collatz Conjecture Sequence')
    plt.legend()
