import matplotlib.pyplot as plt 
import numpy as np


scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=10,
                 color="blue",
                 edgecolor="red")

plt.title("Exam score")
plt.xlabel("scores")
plt.ylabel("# of student")

plt.show()



