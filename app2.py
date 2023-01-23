# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:59:07 2023

@author: Fayis
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 10:30:59 2023

@author: Fayis
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 19:50:20 2023

@author: Fayis
"""



import numpy as np
import pickle
import pandas as pd

import streamlit as st

from PIL import Image


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)



def welcome():
    return "Welcome All"



def predict_note_authentication(variance,skewness,curtosis,entropy):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction
    

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("variance","Type here")
    skewness = st.text_input("sewness","Type here")
    curtosis = st.text_input("curtosis","Type here")
    entropy = st.text_input("entropy","Type here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Let's Learn")
        st.text("Build with StreamLit")
    
if __name__=='__main__':
    main()
    