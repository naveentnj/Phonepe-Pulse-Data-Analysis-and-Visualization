import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

Scatter_Geo_Dataset =  pd.read_csv(r'data/Data_Map_Districts_Longitude_Latitude.csv')
# 20.5937° N, 78.9629
chart_data = pd.read_csv('data/Longitude_Latitude_State_Table.csv')

st.dataframe(chart_data)
st.dataframe(chart_data.describe())
# new = old[['A', 'C', 'D']].copy()
lat_long_data = chart_data[['Latitude','Longitude']]
# rankings_pd.rename(columns = {'test':'TEST'}, inplace = True)
lat_long_data.rename(columns = {'Longitude':'lng','Latitude':'lat'}, inplace = True)
st.dataframe(lat_long_data)
lat_long_data.to_csv('lat_long.csv', index = False)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=20.5937,
        longitude=78.9629,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=2000,
           elevation_scale=400,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))