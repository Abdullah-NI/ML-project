# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model 
loaded_model=pickle.load(open("D:/02 Deploying Model/01DiabetesPrediction/trained_model.sav",'rb'))

input_data=(10,168,74,0,0,38,0.537,34)

#changing data to np array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)


prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):   #pridiction ek list  hai
  print("the person is non diabetic")
else:
  print("the person is diabetic")