import random
import matplotlib.pyplot as plt

data = [random.gauss(0,1)for _ in range(100)]
out=[-10,10]

plt.clf()
plt.boxplot(data, out,vert=False,patch_artist=True)
plt.title('aaaaaa')
plt.xticks(range(-15,16,5))
plt.show()