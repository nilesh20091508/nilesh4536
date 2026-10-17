import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([10, 30, 60, 50])
y2 = np.array([20, 40, 50, 30])
y3 = np.array([30, 50, 60, 25])


title_style = {
    "fontsize": 14,
    "family": "Arial",
    "fontweight": "bold",
    "color": "blue"
}

label_style_blue = {
    "fontsize": 12,
    "family": "Arial",
    "fontweight": "bold",
    "color": "blue"
}

label_style_red = {
    "fontsize": 12,
    "family": "Arial",
    "fontweight": "bold",
    "color": "red"
}

plt.title("Class Size", fontdict=title_style)
plt.xlabel("Year", fontdict=label_style_blue)
plt.ylabel("Students", fontdict=label_style_red)


plt.tick_params(axis="both", colors="red")

plt.plot(x, y1, marker="*", linewidth=2, label="Class A")
plt.plot(x, y2, marker="s", linewidth=2, label="Class B")
plt.plot(x, y3, marker="^", linewidth=2, label="Class C")


plt.xticks(x)
plt.grid(True)
plt.legend()


plt.show()


