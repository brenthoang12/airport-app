import pandas as pd
import streamlit as st
import pydeck as pdk
import numpy as np

st.set_page_config(
    page_title='Airport Map',
    page_icon='🗺️',
)


# ----------------------------------- Define Function
def read_data():
    airport_df = pd.read_csv(
        '/Users/brenthoang/Library/CloudStorage/OneDrive-BentleyUniversity/CS 230/Final Project/airport-codes_csv.csv').set_index(
        'ident')
    return airport_df

def country_list():
    df = read_data()
    extract_country = df['iso_country'].dropna().tolist()
    converted_list = sorted(list(set(extract_country)))
    return converted_list


def convert_data_frame(country):
    df = read_data()
    lat = []
    lon = []
    # convert dataframe with lat and lon
    new_df = df[df['iso_country'] == country][['name', 'type', 'coordinates']]
    coordinate_list = new_df['coordinates'].tolist()
    for i in coordinate_list:
        hold = i.split(', ')
        lat.append(float(hold[1]))
        lon.append(float(hold[0]))
    new_df['lat'] = lat
    new_df['lon'] = lon
    return new_df


def mapping(df):
    map_df = df.filter(['name', 'type', 'lat', 'lon'])
    view_state = pdk.ViewState(latitude=map_df['lat'].mean(),
                               longitude=map_df['lon'].mean(),
                               zoom=8)

    layer = pdk.Layer(type='ScatterplotLayer',
                      data=map_df,
                      get_position='[lon, lat]',
                      get_radius=3000,
                      get_color=[202, 98, 38],
                      pickable=True)

    tool_tip = {'html': 'Airport Name: {name} <br>Type: {type}', 'style': {'backgroundColor': 'white', 'color': 'black'}}

    map = pdk.Deck(map_style='mapbox://styles/mapbox/navigation-day-v1',
                   initial_view_state=view_state,
                   layers=[layer],
                   tooltip=tool_tip)

    st.pydeck_chart(map)


# ----------------------------------- Displayed
st.title(':orange[Airport Map] :world_map:')

user_country = st.selectbox('Select a country', country_list())

airport_df = convert_data_frame(user_country)

mapping(airport_df)
