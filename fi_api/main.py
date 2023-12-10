import arrow
import os
from fastapi import FastAPI
from pytryfi import PyTryFi
from dotenv import load_dotenv

# Load .env file
load_dotenv()

FI_USERNAME = os.getenv("FI_USERNAME")
FI_PASS = os.getenv("FI_PASSWORD")

tryfi = PyTryFi(FI_USERNAME, FI_PASS)
pet = tryfi.pets[0]

app = FastAPI()

@app.get('/location')
def getLocation():
    lat = str(pet.currLatitude)
    lon = str(pet.currLongitude)
    return {'lat': lat, 'lon': lon}

@app.get('/daily-steps')
def dailySteps():
    return {'daily_steps': pet.dailySteps}

@app.get('/weekly-steps')
def dailySteps():
    return {'weekly_steps': pet.weeklySteps}        