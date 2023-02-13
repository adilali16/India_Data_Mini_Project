import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
df =pd.read_csv('India.csv')
list_of_states =list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Data Visualization')
Selected_State =st.sidebar.selectbox('Select a State',list_of_states)
Primary =st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
Secondary =st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))
Plot =st.sidebar.button('Plot Graph')

if Plot:
    st.text('Size Represents Primary Parameter')
    st.text('Color Represents Primary Parameter')
    if Selected_State == 'Overall India':
        fig = px.scatter_mapbox(df,lat="Latitude",lon="Longitude",zoom=4,
                  mapbox_style="carto-positron",size =Primary,color=Secondary,size_max=35
                               ,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == Selected_State]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", zoom=6,
                                mapbox_style="carto-positron", size=Primary, color=Secondary, size_max=35
                                , width=1200, height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
