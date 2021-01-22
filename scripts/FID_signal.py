import numpy as np
import matplotlib.pyplot as plt

num_periods = 10
amp = 10.
T2 = 10

x = np.linspace(np.pi/2., num_periods * 2. * np.pi, num_periods * 100)
y = amp * np.sin(x) * np.exp(-x/T2)

fig=plt.figure(figsize=[5, 5])
ax = fig.add_axes([.1, .1, .8, .8])
ax.plot(x, y)
plt.axis('off')
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
fig.savefig("FID_exp_decay.svg", bbox_inches='tight')
plt.show()
