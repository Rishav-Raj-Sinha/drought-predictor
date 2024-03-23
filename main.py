import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd 
import folium
from streamlit_folium import st_folium
from googletrans import Translator
from languages import *

# translator
#translator = Translator()
#sidebar_heading = translator.translate('Drought-predictor',dest= selected_language)
# sidebar widgets
st.sidebar.write("Drought-predictor")

official_languages_in_india = [
    "English",
    "Hindi",
    "Bengali",
    "Telugu",
    "Marathi",
    "Tamil",
    "Urdu",
    "Gujarati",
    "Kannada",
    "Odia",
    "Punjabi",
    "Malayalam",
    "Assamese",
    "Manipuri",
]
selected_language = st.sidebar.selectbox("Select your language",official_languages_in_india)

states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
selected_state = st.sidebar.selectbox("Select your region",states)

# integrating the map
indian_states_lat = {
    "Andhra Pradesh": "15.9129",
    "Arunachal Pradesh": "28.2180",
    "Assam": "26.2006",
    "Bihar": "25.0961",
    "Chhattisgarh": "21.2787",
    "Goa": "15.2993",
    "Gujarat": "22.2587",
    "Haryana": "29.0588",
    "Himachal Pradesh": "31.1048",
    "Jharkhand": "23.6102",
    "Karnataka": "15.3173",
    "Kerala": "10.8505",
    "Madhya Pradesh": "22.9734",
    "Maharashtra": "19.7515",
    "Manipur": "24.6637",
    "Meghalaya": "25.4670",
    "Mizoram": "23.1645",
    "Nagaland": "26.1584",
    "Odisha": "20.9517",
    "Punjab": "31.1471",
    "Rajasthan": "27.0238",
    "Sikkim": "27.5330",
    "Tamil Nadu": "11.1271",
    "Telangana": "18.1124",
    "Tripura": "23.9408",
    "Uttar Pradesh": "26.8467",
    "Uttarakhand": "30.0668",
    "West Bengal": "22.9868"
}
indian_states_long = {
    "Andhra Pradesh": "79.7400",
    "Arunachal Pradesh": "94.7278",
    "Assam": "92.9376",
    "Bihar": "85.3131",
    "Chhattisgarh": "81.8661",
    "Goa": "74.1240",
    "Gujarat": "71.1924",
    "Haryana": "76.0856",
    "Himachal Pradesh": "77.1734",
    "Jharkhand": "85.2799",
    "Karnataka": "75.7139",
    "Kerala": "76.2711",
    "Madhya Pradesh": "78.6569",
    "Maharashtra": "75.7139",
    "Manipur": "93.9063",
    "Meghalaya": "91.3662",
    "Mizoram": "92.9376",
    "Nagaland": "94.5624",
    "Odisha": "85.0985",
    "Punjab": "75.3412",
    "Rajasthan": "74.2179",
    "Sikkim": "88.5122",
    "Tamil Nadu": "78.6569",
    "Telangana": "79.0193",
    "Tripura": "91.9882",
    "Uttar Pradesh": "80.9462",
    "Uttarakhand": "79.0193",
    "West Bengal": "87.8550"
}
selected_state_lat = indian_states_lat[selected_state]
selected_state_long = indian_states_long[selected_state]
map = folium.Map(location=[selected_state_lat,selected_state_long],zoom_start = 5, tiles = 'CartoDB positron')
st_map = st_folium(map, width=450, height=450)

