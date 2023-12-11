import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
#import seaborn as sns

st.title('2022 MLS Season Visualisations')

#Import the data set
df = pd.read_csv('MLS_performance_data_22_experiment.csv', encoding='latin-1') 

df.drop(['Season','Age (as of 03-20-2023)'], axis=1)

mls_player = st.multiselect('Select MLS players to compare to each other', df['Player'])
player_stats = df[df['Player'].isin(mls_player)]

x_val = st.sidebar.selectbox("Pick your x-axis", df.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis", df.select_dtypes(include=np.number).columns.tolist())

tab1, tab2, tab3 = st.tabs(['Scatter Plot', 'Bar Chart', 'Radar Chart'])

with tab1:
    scatter = alt.Chart(player_stats, title=f"{x_val} and {y_val}").mark_point().encode(
        alt.X(x_val,title=f"{x_val}"),
        alt.Y(y_val,title=f"{y_val}"),
        color = alt.Color('Player', scale=alt.Scale(scheme='darkmulti')),
        #opacity = 50,
        tooltip=[x_val,y_val,'Player']).configure(background='#D9E9F0')
    st.altair_chart(scatter, use_container_width=True)


with tab2:
    bar = alt.Chart(player_stats, title=f"{x_val} and {y_val}").mark_bar().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    color = alt.Color('Player', scale=alt.Scale(scheme='darkmulti')),
    #opacity = 50,
    tooltip=[x_val,y_val,'Player']).configure(background='#D9E9F0')
    st.altair_chart(bar, use_container_width=True)

with tab3:
    import plotly.graph_objects as go
    metrics = ['xG per 90', 'xA per 90', 'Smart passes per 90', 'Key passes per 90', 'Shot assists per 90', 'Goals per 90', 'Touches in box per 90', 'Assists per 90']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
         r = df,
         theta = metrics,
         fill = 'toself',
         name = 'Player A'
    ))
   
    #fig = px.line_polar(player_stats, r=df, theta = metrics, line_close=True)
    st.plotly_chart(fig, use_container_width=True)
#st.dataframe(df)