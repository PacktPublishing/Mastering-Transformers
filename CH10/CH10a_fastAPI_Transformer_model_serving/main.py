import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class QADataModel(BaseModel):
    question: str
    context: str

app = FastAPI()

from transformers import pipeline
model_name = 'distilbert-base-cased-distilled-squad'
model = pipeline(model=model_name, tokenizer=model_name, task='question-answering')

@app.post("/question_answering")
async def qa(input_data: QADataModel):
    result = model(question = input_data.question, context=input_data.context)
    return {"answer": result["answer"]}
if __name__ == '__main__': 
     uvicorn.run('main:app', workers=1) 
