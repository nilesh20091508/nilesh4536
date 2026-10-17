import matplotlib.pyplot as plt 
import numpy as np

x = np.array([1, 2, 3, 4, 5])

figure, axes =plt.subplots(3,2)

axes[0,0].plot(x, x**2, color ="red")
axes[0,0].set_title("*2")

axes[0,1].plot(x, x**2, color ="blue")
axes[0,1].set_title("x**2")

axes[1,0].plot(x, x**3, color ="green")
axes[1,0].set_title("x**3")

axes[1,1].plot(x, x**4, color ="violet")
axes[1,1].set_title("x**4")

axes[2,0].plot(x, x**5, color ="black")
axes[2,0].set_title("x**5")


plt.tight_layout
plt.show()