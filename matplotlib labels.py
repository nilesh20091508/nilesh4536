
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 =np.array([10, 30, 60, 50])
y2 =np.array([20, 40, 50, 30])
y3 =np.array([30, 50, 60, 25])

plt.title("class size", fontsize=20,
                        family="arial",
                        fontweight="bold",
                        color="green"
)                    


plt.xlabel("year", fontsize=20,
                   family="arial",
                   fontweigth="bold",
                   color="green"
)


plt.ylabel("student", fontsize =20,
                      family="arial",
                      fontweight="bold",
                      color="green"
)

plt.tick_params(axis="both",
                colors="green")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()

