import random
numOfStreaks = 0
n = 100

for ex in range(n):
    toss = []
    streaks = 0

    for i in range(100):
        if random.randint(0,1) == 0:
            toss.append('T')
        else:
            toss.append('H')

    for j in range(len(toss)-6):
        if ['H']*6 == toss[j:j+6]:
            numOfStreaks += 1
            streaks += 1
        elif ['T']*6 == toss[j:j+6]:
            numOfStreaks += 1
            streaks += 1
            
    print(streaks)
    
avgStreaks = numOfStreaks/n # streaks per experiment
print(avgStreaks)
