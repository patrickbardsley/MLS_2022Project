import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
#import seaborn as sns

st.title('2022 MLS Season Visualisations')

#Import the data set
df = pd.read_csv('MLS_performance_data_22_experiment.csv', encoding='latin-1') 

df.drop(['Season'])

x_val = st.sidebar.selectbox("Pick your x-axis", df.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis", df.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(df, title=f"{x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    #opacity = 0.5,
    tooltip=[x_val,y_val]).configure(background='#D9E9F0')
st.altair_chart(scatter, use_container_width=True)

#st.dataframe(df)