# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:23:54 2025

@author: affan
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model 
loaded_model=pickle.load(open("D:/02 Deploying Model/01DiabetesPrediction/trained_model.sav",'rb'))

#ceating a function for prediction
def diabetes_prediction(input_data):
    
    #changing data to np array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)


    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):   #pridiction ek list  hai
      return "the person is non diabetic"
    else:
      return "the person is diabetic"
  
    
def main():
    #giving a title
    st.title('Diabetes prediction web app')
    
    
    #getting the input data from  user
    
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('BloodPressure level')
    SkinThickness=st.text_input('SkinThickness value')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('bmi value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    Age=st.text_input('Age of the person')
    
    
    
    #code for prediction
    diagnosis=''
    
    #create a button  fo prediction
    if st.button("Dibetes test prediction"):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)  # give final output
    
    
    
    
if __name__ == '__main__':
    main()
    

    

    