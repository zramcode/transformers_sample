from transformers import pipeline
from fastapi import APIRouter
from pydantic import BaseModel




pipe_sentiment = pipeline(model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

pipe_classification = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")


router = APIRouter(
   
   )


class myrequestmodel(BaseModel):
    input:str

@router.post("/sentiment")
def get_responce(request:myrequestmodel):
    prompt = request.input
    responce = pipe_sentiment(prompt)
    label = responce[0]["label"]
    score = responce[0]["score"]
    return f"The {prompt} input is {label} with a score {score}"

 
@router.post("/text-classification")
def get_responce(request:myrequestmodel):
    prompt = request.input
    responce = pipe_classification(prompt)
    
    return f"The {prompt} input is {responce}"  
    
@router.post("/text-generation")
def get_responce(request:myrequestmodel):
   generator = pipeline("text-generation")
   prompt = request.input
   responce = generator(
       f"base on your answers to question, {prompt} is the best job you can "
        )
   return responce