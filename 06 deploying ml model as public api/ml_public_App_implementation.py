# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:59:22 2025

@author: affan
"""

import json
import requests

url='https://b710-35-226-148-208.ngrok-free.app/diabetes_prediction'  # ye har baar run hone per change hogi link 


input_data_for_model={
    'Pregnancies' : 1,
    'Glucose' : 85,
    'BloodPressure' : 66,
    'SkinThickness' :29,
    'Insulin' : 0,
    'BMI' :26.6,
    'DiabetesPedigreeFunction' : 0.351,
    'Age' : 31
    }


input_json=json.dumps(input_data_for_model)

response=requests.post(url, data=input_json)

print(response.text)