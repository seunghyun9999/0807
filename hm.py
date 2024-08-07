import numpy as np
import matplotlib.pyplot as plt

data =np.random.rand(10,10)

plt.clf()
heatmap = plt.imshow(data,cmap='YlGnBu',aspect='auto')
plt.colorbar(heatmap)
plt.show()

