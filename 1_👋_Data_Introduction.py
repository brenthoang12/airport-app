"""
Name:       Nguyen Minh Quan Hoang
CS230:      Section 4
Data:       Airport
URL:

Description:



Python feature: A function can be called at least 2 places in program, a list comprehension, a function with two or more parameters (one of which has a default value), methods of list, dictionaries or tuples
Streamlit feature: button (Data Introduction), multiselect box (User Interactive Page), select box (User Interactive Page), text input (User Interactive Page)
Visualization: Up to three pie charts (User Interactive Page), One bar chart (User Interactive Page), One map (Airport Map)
Data Analytics Capabilities: Sort (User Interactive Page - Part 1), Filter (User Interactive Page - Part 2), Grouping (User Interactive page - Part 2), Calculator (Part 3)

"""

# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app
# https://towardsdatascience.com/how-to-use-streamlits-st-write-function-to-improve-your-streamlit-dashboard-1586333eb24d
# https://docs.streamlit.io/library/api-reference/text

import pandas as pd
import streamlit as st
import webbrowser
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


# page setup
st.set_page_config(
    page_title='Data Introduction',
    page_icon='✈️',
)

# ----------------------------------- Define Function

# read data
def read_data():
    airport_df = pd.read_csv(
        'airport-codes_csv.csv').set_index(
        'ident')
    return airport_df

# introduction example
def sample_data():
    df = read_data()
    intro_data = df[df['iata_code'].isin(['LAX', 'JFK', 'SIN', 'LHR', 'CDG'])]
    return intro_data


# ----------------------------------- Displayed
st.title(':orange[Airport Around the World] :small_airplane:')

airport_image = Image.open(
    'changi_airport.jpeg')
st.image(airport_image, caption='Changi Airport by Wikipedia')

st.write(
    "As of September 2021, there were **over 40,000 airports around the world** (World Bank's World Development Indicators)."
    " The number included all types of airport, including military, private, and unpaved airstrips, and commercial airports. "
    "According to Airports Council International (ACI), which is the global trade representative of the world's airports, there "
    "were **17,678 commercial airports** in the world as of 2020.")

# Data Introduction
st.header("Our Data :passport_control:")

st.write(sample_data())
st.caption(":warning: **Please be aware. Not all airports have the information for all column recorded.**")

st.write("**“data/airport-codes.csv”** contains the list of all airport codes (over 50,000), the attributes are identified in datapackage "
         "description. Some of the columns contain attributes identifying airport locations, other codes (IATA, local if "
         "exist) that are relevant to identification of an airport.")

st.write("- **ident code**: airport four-digit code assigned by International Civil Aviation Organization (ICAO) used for "
         "air traffic control and other aviation-related purposes")
st.write("- **type**: type of airport, such as heliport, small_airport, large_airport and closed")
st.write("- **elevation_ft**:  the height of an airport's runway above mean sea level (MSL) in feet")
st.write("- **iata_code**: most commonly used airport three-digit code assigned by International Air Transport Association (IATA)")


data_link = 'https://datahub.io/core/airport-codes#readme'
if st.button('Data link', key='small-button'):
    webbrowser.open_new_tab(data_link)




