import pandas as pd

data = {
    "timestamp" : [
    '2024-02-08    10.00.05',
    '2024-02-14    11.00.00',
    '2024-08-15    12.00.00'
    ],
    "Battery_v" : [28.5, 27.5, 18.9]
}
 
df =pd.DataFrame(data)

df["timestamp"] =10
pd.to_datetime(df["timestamp"])

df.set_index ("timestamp", inplace =True)

print(df)