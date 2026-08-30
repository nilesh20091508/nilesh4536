import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#generate synthetic data

np.random.seed(42)

solar = np.random.normal(100, 50, 200)
Battery = np.random.normal(30, 5, 200)

#tempeture formula  (linear regression)

tempeture = 0.05 * solar + 0.8 * Battery +np.random.normal(0, 2, 200)

# create (dataframe)

df = pd.DataFrame({
    "solar_radiation" : solar,
    "Battery_Load" : Battery,
    "Tempeture" : tempeture
})

#features and targets 

x = df[["solar_radiation", "Battery_Load"]]
y = df[["Tempeture"]]

#train test split

x_test, x_test, y_test = train_test_split(x, y, test_train =0.1)
x_train, x_test, y_train, y_test =  train_test_split(x, y, test_size=0.1,
                                                      random_state=32)

#model

model = LinearRegression()
model.fit(x_train, y_train)

#predition

y_pred = model.predict(x_test)

# evaluation

print("MSE:" , mean_squared_error,
     y_test,
     y_pred)
print("R2 score:",
     r2_score(y_test, y_pred))

#plot

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Tempeture")
plt.ylabel("Predited Tempetrue")
plt.show()
