from sklearn.linear_model import LinearRegression
import numpy as np

# study hours (input)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# marks obtained (output)
y = np.array([35, 40, 50, 60, 70])

# create model
model = LinearRegression()

# train model
model.fit(X, y)

# predict marks for 6 hours study
predicted_marks = model.predict([[6]])

print("Predicted marks for 6 hours study:", predicted_marks[0])
