import matplotlib.pyplot as plt

amt = 6346
nday = 5 * 365
avg = []
day = []
for i in range(1, nday):
    cost = amt / i
    avg.append([cost])
    day.append([i])
plt.plot(day,avg,color='r')
plt.show()
