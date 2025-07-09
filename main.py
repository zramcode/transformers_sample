from fastapi import FastAPI
from pipline_test import test_pipeline
from datasets_test import test_dataset
app = FastAPI()

app.include_router(test_pipeline.router)
app.include_router(test_dataset.router)