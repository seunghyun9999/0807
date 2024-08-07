import pandas as pd
import numpy
import matplotlib.pyplot as plt
import random

x=[random.uniform(0,100)for _ in range(100)]
y=[2*val + 1 + random.uniform(-10,10)for val in x]

xline =range(101)
yline =[2*val+1for val in xline]
plt.clf()
fig, ax = plt.subplots()

plt.scatter(x,y, label='random',color='gold',marker='*',
            s=30, alpha=0.5)

plt.plot(xline,yline,label='r',color='green')
ax.set_facecolor('black')
plt.xlabel('star')
plt.ylabel('y')
plt.show()

