import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]
z = [2,3,4,5,6]
 
plt.grid(axis="y",
         linewidth=1,
         color="blue",
         linestyle="dashed")

plt.plot(x,y,z)

plt.show()