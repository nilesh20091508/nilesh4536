import matplotlib.pyplot as plt 
import numpy as np


categorie = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = [300, 250, 275, 226]
colors = ["red", "yellow", "green", "blue"]

plt.pie(values, labels = categorie,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0,0,0,0.2],
                shadow=True,
                startangle=180)
                

plt.title("PIE CHART")
plt.show()