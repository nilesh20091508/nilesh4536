import matplotlib.pyplot as pld
import numpy as np

categories = np.array(["grains", "fruits", "vegetables", "dairy", "protein", "sweets"])
values = np.array([9, 7, 5, 4, 6, 8])

pld.bar(categories, values)

pld.title("daily consuption")
pld.xlabel("Food")
pld.ylabel("Quantity")


pld.show()