from fastapi import FastAPI, Query, Path
import random

app = FastAPI()
@app.get("/temperature")
def temperature(location: str = Query(..., description="Location")):
    return random.randint(0, 50)

@app.get("/temperature/{location}")
def temperature_2(location: str = Path(..., description="Location")):
    return {"value": random.randint(0, 50)}