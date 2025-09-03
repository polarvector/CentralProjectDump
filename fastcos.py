import time
import math
import matplotlib.pyplot as plt

def fastcos1(x):
    a = x**2
    return 1 - a/2 + (a*a)/24 - (a*a*a)/720

def fastcos2(x):
    a = x**2
    return 1 - (360 - a * (30 - a)) * a / 720

def comparison(n):
    start = time.time()
    for i in range(n):
        val = fastcos1(i / n)
    fastcos1time = time.time() - start

    start = time.time()
    for i in range(n):
        val = fastcos2(i / n)
    fastcos2time = time.time() - start

    start = time.time()
    for i in range(n):
        val = math.cos(i / n)
    fastcosbasetime = time.time() - start

    # Avoid division by zero
    if fastcos1time == 0:
        fastcos1time = 1e-10
    if fastcosbasetime == 0:
        fastcosbasetime = 1e-10

    return (fastcos2time / fastcos1time) * 100, (fastcos2time / fastcosbasetime) * 100

fastfast = []
fastbase = []
meanff = []
meanfb = []
m = 100

for k in range(100000, 100000 + m):
    a, b = comparison(k)
    fastfast.append(a)
    fastbase.append(b)
    # Calculate the moving average
    if k == 100000:
        meanff.append(a)
        meanfb.append(b)
    else:
        meanff.append((meanff[-1] * (k - 100000) + a) / (k - 100000 + 1))
        meanfb.append((meanfb[-1] * (k - 100000) + b) / (k - 100000 + 1))

plt.plot(range(100000, 100000 + m), meanff, label='Moving Average fastfast')
plt.plot(range(100000, 100000 + m), meanfb, label='Moving Average fastbase')
plt.legend()
plt.show()
