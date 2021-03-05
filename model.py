from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import pickle


X, y = load_boston(return_X_y=True)
model = LinearRegression().fit(X, y)
print(X,y)

pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)

# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)


print(pickle_model.predict(X))