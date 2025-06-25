from transformers import pipeline
from fastapi import APIRouter
from pydantic import BaseModel



pipe = pipeline(model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")


router = APIRouter(
   prefix="/sentiment",
   tags= ["Sentiments"]
   )


class myrequestmodel(BaseModel):
    input:str

@router.post("/")
def get_responce(request:myrequestmodel):
    prompot = request.input
    responce = pipe(prompot)
    label = responce[0]["label"]
    score = responce[0]["score"]
    return f"The {prompot} input is {label} with a score {score}"