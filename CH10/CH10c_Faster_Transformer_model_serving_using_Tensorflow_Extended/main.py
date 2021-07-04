import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import BertTokenizerFast, BertConfig
import requests
import json
import numpy as np

tokenizer = BertTokenizerFast.from_pretrained("nateraw/bert-base-uncased-imdb")
config = BertConfig.from_pretrained("nateraw/bert-base-uncased-imdb")


class DataModel(BaseModel):
    text: str

app = FastAPI()

@app.post("/sentiment")
async def sentiment_analysis(input_data: DataModel):
    print(input_data.text)
    tokenized_sentence = [dict(tokenizer(input_data.text))]
    data_send = {"instances": tokenized_sentence}
    response = requests.post("http://localhost:8501/v1/models/bert:predict", data=json.dumps(data_send))
    result = np.abs(json.loads(response.text)["predictions"][0])
    return {"sentiment": config.id2label[np.argmax(result)]}


if __name__ == '__main__': 
     uvicorn.run('main:app', workers=1) 
