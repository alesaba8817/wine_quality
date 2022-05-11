import pandas as pd
import pickle


class Model:
    def __init__(self, item:pd.DataFrame):
        self.item = item
        self.model = pickle.load(open("random_forest_00.sav", "wb"))

    def predict(self):
        return self.model.predict(self.item)