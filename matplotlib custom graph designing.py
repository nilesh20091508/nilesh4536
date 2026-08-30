import matplotlib.pyplot as plt
import numpy as np


x = np.array([2023, 2024, 2025, 2026])
y1 =np.array([10, 30, 60, 50])
y2 =np.array([20, 40, 50, 30])
y3 =np.array([30, 50, 60, 25])
y4 =np.array([40, 50, 30, 20])
y5 =np.array([50 ,60, 70, 25])
y6 =np.array([10, 30, 12, 15])
y7 =np.array([20, 30, 50 ,60])

line_style = dict(marker = "*",
                 markersize = 10,
                 markerfacecolor = "#FF0000",
                 markeredgecolor = "#00000046",
                 linestyle = "solid",
                 linewidth = 4,
)


plt.plot(x, y1, color= "cyan", **line_style)
plt.plot(x, y2, color= "grey", **line_style)
plt.plot(x, y3, color= "orange", **line_style)
plt.plot(x, y4, color= "magenta", **line_style)
plt.plot(x, y5, color= "darkblue", **line_style)
plt.plot(x, y6, color=  "teal", **line_style)
plt.plot(x, y7, color= "red",  **line_style)

plt.show()

