from fastapi import FastAPI, Query
import random

app = FastAPI()
@app.get("/temperature")
def temperature(location: str = Query(..., description="Location")):
    temperature_now = round(random.uniform(0, 40), 1)
    return temperature_now