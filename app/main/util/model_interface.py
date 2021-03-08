from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import pickle


X, y = load_boston(return_X_y=True)
model = LinearRegression().fit(X, y)

pkl_filename = "./app/main/static/models/pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)

class HousePriceModel():
    def __init__(self):
        # Load from file
        with open(pkl_filename, 'rb') as file:
            self.pickle_model = pickle.load(file)

    def predict(self,X):
        """
        :param X: [[feature1,feature2,feature3..featuren]]
        """
        pred = self.pickle_model.predict([X])
        return pred