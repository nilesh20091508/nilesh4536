import matplotlib.pyplot as plt
import numpy as np


x1  = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y1  = np.array([55, 45, 67, 33, 66, 67, 45, 78, 56])

x2 = np.array([0, 1, 1, 2, 3, 4, 4, 5, 6,])
y2 = np.array([58, 59, 45, 20 , 30, 45 ,65, 66, 76])


plt.scatter_3d(x1,y1,
                 color="darkblue",
                 alpha=0.5,
                 s =100,
                 label=("class A"))



plt.scatter_3d(x2,y2,
                color="Red",
                 alpha=0.5,
                 s =100,              
                 label=("class B"))



plt.title("test scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend

plt.show()