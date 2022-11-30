from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 

st.markdown(" <centre>  <h1> LUDO </h1> </font>    </centre> </h1> ",unsafe_allow_html=True)

A=st.number_input   ('Enter Abdallah`s Score') 
M=st.number_input    ('Enter Mona`s Score')


data_I= pd.DataFrame([A,M],index = ['Abdallah','Mona'], columns=['Score'])
data_I = data_I.reset_index().rename(columns = {'index':'Player Name'})
Total = A+M
data_II = pd.DataFrame([((A/Total)*100),((M/Total)*100)],columns=['Score %'])
data_II=data_II.rename(columns = {'0':'index'})

data_III = pd.concat([data_I,data_II], axis = 1)
 
if Total >0: 
  st.write(data_III)

  fig= px.bar(data_I, y = 'Score' ) 
  st.plotly_chart(fig, use_container_width=True)

  # streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Test\\LUDO.py"

  st.write(f'The Total Matches = {A+M} ')

  st.write(f'The Total Matches of Abdallah  = {A}  Matches with Percentage {(A/Total)*100} %')
  st.write(f'The Total Matches of Abdallah  = {M}  Matches with Percentage {(M/Total)*100} %')







