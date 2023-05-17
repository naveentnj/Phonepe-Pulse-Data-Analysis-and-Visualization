# https://deckgl.readthedocs.io/en/latest/gallery/hexagon_layer.html

import pydeck as pdk
import streamlit as st
import pandas as pd
import numpy as np


HEXAGON_LAYER_DATA = ('lat_long.csv')

# Define a layer to display on a map
layer = pdk.Layer(
    "HexagonLayer",
    HEXAGON_LAYER_DATA,
    get_position=["lng", "lat"],
    auto_highlight=True,
    elevation_scale=5000,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1,
)

# Set the viewport location
view_state = pdk.ViewState(
    longitude=-1.415,
    latitude=52.2323,
    zoom=6,
    min_zoom=5,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36,
)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
st.pydeck_chart(r)

#r.to_html("hexagon_phonepe_data_layer.html")