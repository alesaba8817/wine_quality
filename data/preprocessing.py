import pandas as pd

from data.jsonschema import Item

class Preprocess:
    def __init__(self, item:Item):
        self.item = item

    def to_dataframe(self) -> pd.DataFrame:
        dict_input = dict()
        dict_input["fixed_acidity"] =self.item.fixed_acidity
        dict_input["volatile_acidity"] = self.item.volatile_acidity
        dict_input["citric_acid"] = self.item.citric_acid
        dict_input["residual_sugar"] = self.item.residual_sugar
        dict_input["chlorides"] = self.item.chlorides
        dict_input["free_sulfur_dioxide"] = self.item.free_sulfur_dioxide
        dict_input["total_sulfur_dioxide"] = self.item.total_sulfur_dioxide
        dict_input["density"] = self.item.density
        dict_input["pH"] = self.item.pH
        dict_input["sulphates"] = self.item.sulphates
        dict_input["alcohol"] = self.item.alcohol
        return pd.DataFrame().from_dict(dict_input, orient="records")