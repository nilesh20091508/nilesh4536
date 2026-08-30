import pandas as pd
import numpy as np

data = {
    "Timestamp":
pd.date_range(start = "2026-01-01", periods = 200, freq = "min"),
    "Tempeture_C" : np.random.normal(24, 8, 200),
    "Battery_voltage" : np.random.normal(30, 2, 200),
    "Current_A" : np.random.normal(24, 8, 200),
    "Signal_strength_dB" : np.random.normal (70 , 3, 200),
    "Alitude_km" : np.random.normal (500,  50, 200)

 }

df = pd.DataFrame(data)
print(df.head())