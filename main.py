from fastapi import FastAPI
from pipline_test import test_pipeline

app = FastAPI()

app.include_router(test_pipeline.router)