import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
#import seaborn as sns

st.title('2022 MLS Season Player Data - Visualised')

st.markdown("**Statistics for every MLS player that played during the 2022 MLS Season.**")

#Import the data set
df = pd.read_csv('MLS_performance_data_22_experiment.csv', encoding='latin-1') 

df.drop(['xG', 'xA'], axis=1)

st.sidebar.header("Pick two player metrics for your charts: ")
x_val = st.sidebar.selectbox("Pick your x-axis", df.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis", df.select_dtypes(include=np.number).columns.tolist())

mls_player = st.multiselect('Select MLS players to compare to each other', df['Player'])
player_stats = df[df['Player'].isin(mls_player)]

tab1, tab2, tab3 = st.tabs(['Scatter Plot', 'Bar Chart', 'Heatmap'])

with tab1:
    scatter = alt.Chart(player_stats, title=f"{x_val} and {y_val}").mark_point().encode(
        alt.X(x_val,title=f"{x_val}"),
        alt.Y(y_val,title=f"{y_val}"),
        color = alt.Color('Player', scale=alt.Scale(scheme='darkmulti')),
        #opacity = 50,
        size=alt.Size('Player', scale=alt.Scale(range=[100, 500])),
        tooltip=[x_val,y_val,'Player','Position']).configure(background='#D9E9F0')
    st.altair_chart(scatter, use_container_width=True)

with tab2:
    bar = alt.Chart(player_stats, title=f"{x_val} and {y_val}").mark_bar(size=20).encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    color = alt.Color('Player', scale=alt.Scale(scheme='darkmulti')),
    #opacity = 50,
    tooltip=[x_val,y_val,'Player']).configure(background='#D9E9F0')
    st.altair_chart(bar, use_container_width=True)

with tab3:
    heatmap = alt.Chart(player_stats).mark_rect().encode(
        alt.X(x_val).bin(maxbins=50),
        alt.Y(y_val).bin(maxbins=30),
        alt.Color('Player').scale(scheme='darkmulti')
    )
    st.altair_chart(heatmap, use_container_width=True)

# with tab3:
#     import plotly.graph_objects as go
#     metrics = ['xG per 90', 'xA per 90', 'Smart passes per 90', 'Key passes per 90', 'Shot assists per 90', 'Goals per 90', 'Touches in box per 90', 'Assists per 90']
#     xG_per_90 = df[df['xG per 90'].isin(mls_player)]
#     smart_passes_per_90 = df[df['Smart passes per 90'].isin(mls_player)]
#     key_passes_per_90 = df[df['Key passes per 90'].isin(mls_player)]
#     shot_assists_per_90 = df[df['Shot assists per 90'].isin(mls_player)]
#     goals_per_90 = df[df['Goals per 90'].isin(mls_player)]
#     touches_in_box_per_90 = df[df['Touches in box per 90'].isin(mls_player)]
#     assists_per_90 = df[df['Assists per 90'].isin(mls_player)]
#     radar_chart_info = [xG_per_90, smart_passes_per_90, key_passes_per_90, shot_assists_per_90, goals_per_90, touches_in_box_per_90, assists_per_90]

#     fig = go.Figure()

#     fig.add_trace(go.Scatterpolar(
#          r = [xG_per_90, smart_passes_per_90, key_passes_per_90, shot_assists_per_90, goals_per_90, touches_in_box_per_90, assists_per_90],
#          theta = metrics,
#          fill = 'toself',
#          name = 'Player A'
#     ))
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(
#                 visible=True
#             ),
#         ),
#         showlegend=False
#     )
   
#     #fig = px.line_polar(player_stats, r=radar_chart_info, theta = metrics, line_close=True)
#     st.plotly_chart(fig, use_container_width=True)
# #st.dataframe(df)