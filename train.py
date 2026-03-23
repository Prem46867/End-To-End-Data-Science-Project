import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("Task3\data\salary.csv")

X = data[['experience']]
y = data['salary']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model created")
