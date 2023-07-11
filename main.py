import random

freqs = {}
sim = 10000
    
for i in range(sim):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    if sum in freqs: 
        freqs[sum] += 1
    else:
        freqs[sum] = 1
    
for freq in range(2,13):
    if freqs.get(freq) == None:
        freqs[freq] = 0
    
    if freq < 10:
        output = '0'
    else:
        output = ''
    output += f"{freq}: "
    for i in range(round(freqs.get(freq)/sim*100)):
        output += '*'
    
    print(output)