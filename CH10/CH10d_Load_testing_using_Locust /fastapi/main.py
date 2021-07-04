import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class DataModel(BaseModel):
    text: str

app = FastAPI()

from transformers import pipeline
model_name = 'nateraw/bert-base-uncased-imdb'
model = pipeline(model=model_name, tokenizer=model_name, task='sentiment-analysis')

@app.post("/sentiment")
async def predict(input_data: DataModel):
    result = model(input_data.text)[0]
    return result
if __name__ == '__main__': 
     uvicorn.run('main:app', workers=1) 
