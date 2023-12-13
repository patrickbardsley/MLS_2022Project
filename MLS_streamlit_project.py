import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
#import seaborn as sns



#Import the data set
df = pd.read_csv('MLS_performance_data_22_experiment.csv', encoding='latin-1') 
st.set_page_config(layout="wide")
st.title('2022 MLS Season Player Data - Visualised')
st.markdown("**Statistics for every MLS player that played during the 2022 MLS Season.**")

st.sidebar.header("Pick two player metrics for your charts: ")
x_val = st.sidebar.selectbox("Pick your x-axis", df.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis", df.select_dtypes(include=np.number).columns.tolist())


mls_player = st.multiselect('Select MLS players to compare to each other', df['Player'])
all_options = st.checkbox("Select all players")
if all_options:
    mls_player = df['Player']
player_stats = df[df['Player'].isin(mls_player)]


#position_box = st.sidebar.selectbox('Select a particular position', df['Position'].drop_duplicates())
#position = df[df['Position']==(position_box)]
#min_matches_played = df['Matches played']
#min_matches_played_display = st.sidebar.number_input("Enter a value between 1 and 38 to determine the mimimum number of matches played in order to be displayed", min_value=1, max_value=len(min_matches_played), value=20,step=1)


tab1, tab2, tab3 = st.tabs(['Scatter Plot', 'Bar Chart', 'Heatmap'])

with tab1:
    scatter = alt.Chart(player_stats, title=f"{x_val} and {y_val}").mark_point().encode(
        alt.X(x_val,title=f"{x_val}"),
        alt.Y(y_val,title=f"{y_val}"),
        color = alt.Color('Player', scale=alt.Scale(scheme='darkmulti')),
        size=alt.Size('Player', scale=alt.Scale(range=[100, 500])),
        tooltip=[x_val,y_val,'Player','Position']).configure(background='#D9E9F0')
    st.altair_chart(scatter, use_container_width=True)

with tab2:
    bar = alt.Chart(player_stats, title=f"{x_val} and {y_val}").mark_bar(size=20).encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    color = alt.Color('Player', scale=alt.Scale(scheme='darkmulti')),
    tooltip=[x_val,y_val,'Player','Position']).configure(background='#D9E9F0')
    st.altair_chart(bar, use_container_width=True)

with tab3:
    heatmap = alt.Chart(player_stats, title=f"{x_val} and {y_val}").mark_rect().encode(
        alt.X(x_val,title=f"{x_val}").bin(maxbins=10),
        alt.Y(y_val,title=f"{y_val}").bin(maxbins=10),
        alt.Color('Player').scale(scheme='darkmulti')
    ).configure(background='#D9E9F0')
    st.altair_chart(heatmap, use_container_width=True)