import pandas as pd

data ={
    "Timestamp":
    pd.to_datetime ([
        "2024-06-01 10:00:00", 
        "2024-06-02 11:00:00",
        "2024-06-03 12:00:00"
    ]),
    "value" : [10,60,80]
}

df = pd.DataFrame(data)
print(df)

