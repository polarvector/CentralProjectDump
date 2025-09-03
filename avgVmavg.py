import numpy as np
import matplotlib.pyplot as plt
import random

allnums = []
elements = 100 # no. of elements to check
mavg = 0
plt.figure()
mvg = []
start = 0
stop = 100

for i in range(elements):
    num = float(random.randint(start,stop))
    allnums.append(num)

    if i==0:
        mavg = num
        mvg.append(mavg)
        continue
    elif i==1:
        mavg = mavg+num
        mvg.append(mavg)
        continue
    else:
        mavg = (i*mavg+num)/(i+1)
        mvg.append(mavg)
        
trueavg = sum(allnums)/len(allnums)
iteration = np.linspace(1,elements,elements)

plt.subplot(2,1,1), plt.plot(iteration, mvg, label='True Running Average')
plt.plot(np.linspace(1,elements,elements),np.ones(elements)*trueavg, label='Final Average Line')
plt.legend(loc="upper right"); plt.ylim([start,stop])

plt.subplot(2,1,2), plt.plot(iteration, 100*abs(mvg-trueavg*np.ones(elements))/(trueavg*np.ones(elements)),label='% Error')
plt.ylim([0,100]); plt.legend(loc="upper right"); plt.show()
