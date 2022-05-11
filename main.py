from fastapi import FastAPI

from data.jsonschema import Item
from data.preprocessing import Preprocess
from models.models import Model

app = FastAPI()

@app.post('/predict')
async def predict(item:Item) -> float:
    return Model(Preprocess(item).to_dataframe()).predict()