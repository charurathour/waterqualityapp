# -*- coding: utf-8 -*-
import pickle
import numpy as np
import streamlit as st

loaded_model=pickle.load(open("random_forest.sav",'rb'))

def water_quality(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0]==0):
        return 'Water quality is good'
    else:
        return 'Water quality is bad'
    
def main():
    st.title('Water Quality Prediction')
    
    ph=st.text_input('PH value','Type here')
    Hardness=st.text_input('Hardness value','Type here')
    Solids=st.text_input('Solids value','Type here')
    Chloramines=st.text_input('Chloramines value','Type here')
    Sulfate=st.text_input('Sulfate value','Type here')
    Conductivity=st.text_input('Conductivity value','Type here')
    Organic_carbon=st.text_input('Organic carbon value','Type here')
    Trihalomethanes=st.text_input('Trihalomethanes value','Type here')
    Turbidity=st.text_input('Turbidity value','Type here')
    
    diagnosis=''
    
    if st.button('Check Water Quality'):
        diagnosis=water_quality([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
        
    st.success(diagnosis)
    
if __name__ =='__main__':
    main()
        
    