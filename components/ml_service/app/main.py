# Data Handling
import pickle
import numpy as np
import pandas as pd
from pydantic import BaseModel

# Server
import uvicorn
from fastapi import FastAPI

# Modeling
from xgboost import XGBClassifier

app = FastAPI()

# Initialize files
classifier_model = pickle.load(open('xgboost_classifier.pickle', 'rb'))

features_columns = ['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident', 'left',
       'promotion_last_5years', 'sales_RandD', 'sales_accounting', 'sales_hr',
       'sales_management', 'sales_marketing', 'sales_product_mng',
       'sales_sales', 'sales_support', 'sales_technical']

def convert_dummies(to_predict, expected_model_columns, categorical_variables):
    new_dict = to_predict.copy()
    for v in categorical_variables:
        new_dict.update({'{categorical}_{value}'.format(categorical=v, value=new_dict.get(v)): 1})
        new_dict.pop(v)
    
    dependent_variables = []
    for feature in expected_model_columns:
        dependent_variables.append(new_dict.get(feature, 0))

    return np.array(dependent_variables)

class Data(BaseModel):
    satisfaction_level: float
    last_evaluation: float
    number_project: float
    average_montly_hours: float
    time_spend_company: float
    Work_accident: float
    promotion_last_5years: float
    sales: str

@app.get('/msg')
def read_something():
    return {'msg': "Hello world!"}

@app.post("/predict")
def predict_api(data: Data):
    
    # Extract data in correct order
    data_dict = data.dict()
     
    # Apply encoding
    encoded_features = convert_dummies(
        to_predict=data_dict,
        expected_model_columns=features_columns,
        categorical_variables=['sales'])

    
    # Create and return prediction
    prediction = classifier_model.predict(encoded_features.reshape(1, -1))

    return {"prediction": prediction[0]}