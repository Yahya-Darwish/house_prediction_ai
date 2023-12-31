# 1. Library imports

from fastapi import FastAPI
import numpy as np
import pickle as pk
import pandas as pd
from Property import Property
from fastapi.middleware.cors import CORSMiddleware

# 2. Create the app object

import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
classifier_RFR = pk.load(open("model_RFR.pkl" , "rb"))

# 3. Expose the prediction functionality, make a prediction from the passed

@app.post('/predict')
def predict_property_price(data:Property):
    data = dict(data)
    bedrooms=data['bedrooms']
    bathrooms=data['bathrooms']
    sqft_living=data['sqft_living']
    sqft_lot=data['sqft_lot']
    floors=data['floors']
    waterfront=data['waterfront']
    view=data['view']
    condtion=data['condtion']
    grade=data['grade']
    sqft_above=data['sqft_above']
    sqft_basement=data['sqft_basement']
    yr_built=data['yr_built']
    yr_renovated=data['yr_renovated']
    zipcode=data['zipcode']
    lat=data['lat']
    sqft_living15=data['sqft_living15']
    sqft_lot15=data['sqft_lot15']
   # print
    prediction = classifier_RFR.predict([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condtion,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,sqft_living15,sqft_lot15]])[0]
    return {
        'prediction': prediction
    }
