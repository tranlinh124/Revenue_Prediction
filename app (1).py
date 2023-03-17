import streamlit as st
import numpy as np
import sklearn
import pickle

model = pickle.load(open('model.pickle', "rb"))

st.title('REVENUE PREDICTION')

Tempt= st.number_input('Input Temperature')
Tempt = np.array(Tempt).reshape(-1, 1)
if st.button('Predict'):
  Result = model.predict(Tempt)
  st.text('Revenue Prediction')
  st.success(Result)