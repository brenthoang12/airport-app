import pandas as pd
import streamlit as st
import webbrowser
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# page setup
st.set_page_config(
    page_title='User Interactive Page',
    page_icon='⚒️',
)

# Set the configuration options for Matplotlib
st.set_option('deprecation.showPyplotGlobalUse', False)


# ----------------------------------- Define Function
# read data
def read_data():
    airport_df = pd.read_csv(
        '/Users/brenthoang/Library/CloudStorage/OneDrive-BentleyUniversity/CS 230/Final Project/airport-codes_csv.csv').set_index(
        'ident')
    return airport_df

# get all countries into a list and sort
def country_list():
    df = read_data()
    extract_country = df['iso_country'].dropna().tolist()
    converted_list = sorted(list(set(extract_country)))
    return converted_list

# filter data
def filter_data(selected_country):
    df = read_data()
    filter_country_data = df[df['iso_country'].isin(selected_country)]
    return filter_country_data

# count number of airport in the country
def count_airport(df, selected_country=['US', 'CA', 'JP']):
    number_airport_in_country = [df[df['iso_country'].isin([i])].shape[0] for i in selected_country]
    return number_airport_in_country


# get country data
def country_airport(user_input):
    df = read_data()
    airport = df[df['iso_country'] == user_input][['iata_code', 'type', 'name', 'continent', 'iso_region', 'municipality', 'coordinates']]
    return airport


# bar chart: number of airport in each country
def generate_bar_chart(selected_country):
    # convert number of airport and country in to a data frame
    filter_country = filter_data(selected_country)
    number_of_airport = count_airport(filter_country, selected_country)
    dictAIR = {'country': selected_country, 'airports': number_of_airport}
    df = pd.DataFrame(dictAIR)

    # max number of airport
    max_airport = df['airports'].max()
    colors = ['#268eca' if x != max_airport else '#ca6226' for x in df['airports']]

    # create a bar chart
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.bar(df['country'], df['airports'], color=colors)
    ax.set_title('Number of Airports in Country', fontsize=5)
    ax.set_xlabel('Country', fontsize=5)
    ax.set_ylabel('Airports', fontsize=5)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)
    st.pyplot(fig)


# pie chart: type of airport in each country
def generate_pie_chart(countries):
    df = read_data()
    for i in range(len(countries)):
        # extract type
        type_list = df[df['iso_country'] == countries[i]]['type'].dropna().tolist()
        # convert to a dict
        type_count = {x: type_list.count(x) for x in set(type_list)}
        # pie chart
        labels = list(type_count.keys())
        values = list(type_count.values())
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        ax.set_title(f'Types of Airport in {countries[i]}')
        st.pyplot(fig)


# elevation table
def elevation_table(country):
    df = read_data()
    # extract elevation
    elevation_list = df[df['iso_country'] == country]['elevation_ft'].dropna().tolist()
    elevation_list1 = [int(x) for x in elevation_list]
    print('There are', len(elevation_list1), 'in', country)
    elevation_dict = {'Min': round(min(elevation_list1), 0), 'Avg': round(sum(elevation_list1)/len(elevation_list1), 0), 'Max': round(max(elevation_list1), 0)}
    elevation_df = pd.DataFrame.from_dict(elevation_dict, orient='index', columns=['Elevation'])

    st.write(elevation_df)

# ----------------------------------- Displayed

st.title(':orange[User Interactive Space] :hammer_and_wrench:')

airport_image = Image.open(
    '/Users/brenthoang/Library/CloudStorage/OneDrive-BentleyUniversity/CS 230/Final Project/denver_airport.webp')
st.image(airport_image, caption='Denver Airport by George Rose')

st.write("In this page, you can customize data according to your interest. The first part is dedicated to "
         "**extracting airports data** from a selected country. The second part is for **comparing two or three countries "
         "number of airports**, and analyzing airport type of each country on a pie chart. The third part is similar "
         "to the first part but we will find the average **airport elevation** and find what airports are highest and lowest "
         "compared to sea level in a country.")

list_of_countries = country_list()

# Part 1
st.header('Extracting Data :speech_balloon:')
user_countries1 = st.selectbox('Select a country', list_of_countries)
st.write(country_airport(user_countries1))

# Part 2
st.header('Comparing Airports :bar_chart:')
user_countries2 = st.multiselect('Select up to three countries', list_of_countries, ['US', 'CA', 'JP'], max_selections=3)
generate_bar_chart(user_countries2)
generate_pie_chart(user_countries2)

# Part 3
st.header('Airport Elevation :airplane_arriving:')
st.write('For this section, you could choose a country ad find its airports max, min and average elevation in feet.')
user_countries3 = st.text_input('Select a country', 'JP')
elevation_table(user_countries3)
