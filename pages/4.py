import streamlit as st
import pandas as pd 
import folium
from streamlit_folium import st_folium
from googletrans import Translator
from languages import *
import module
import numpy as np
from scipy.stats import gamma
from scipy.stats import norm
import matplotlib.pyplot as plt
import selectedlang
import selectedstate
from prophet import Prophet
import json
#page config
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
hide_decoration_bar_style = '''<style>header {visibility: hidden;}
</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

selected_language = selectedlang.selected_language
selected_state = selectedstate.selected_state

csv = ""
if selected_state == "Arunachal Pradesh":
    csv = "Arunachal pradesh.csv"
elif selected_state == "Andhra Pradesh":
    csv = "Andhra pradesh.csv"
elif selected_state == "Assam":
    csv = "Assam.csv"
elif selected_state == "Chhattisgarh":
    csv = "Chhattisgarh.csv"
elif selected_state == "Goa":
    csv = "Goa.csv"
elif selected_state == "Gujarart":
    csv = "Gujarat.csv"
elif selected_state == "Harayana":
    csv = "Harayana.csv"
elif selected_state == "Himachal Pradesh":
    csv = "Himachal Pradesh.csv"
elif selected_state == "Jharkhand":
    csv = "Jharkhand.csv"
elif selected_state == "Karnataka":
    csv = "Karnataka.csv"
elif selected_state == "Kerala":
    csv = "Kerala.csv"
elif selected_state == "Madhya Pradesh":
    csv = "Madhya Pradesh.csv"
elif selected_state == "Maharasthra":
    csv = "Maharashtra.csv"
elif selected_state == "Manipur":
    csv = "Manipur.csv"
elif selected_state == "Meghalaya":
    csv = "Meghalaya.csv"
elif selected_state == "Mizoram":
    csv = "Mizoram.csv"
elif selected_state == "Nagaland":
    csv = "Nagaland.csv"
elif selected_state == "Odisha":
    csv = "Odisha.csv"
elif selected_state == "Punjab":
    csv = "Punjab.csv"
elif selected_state == "Rajasthan":
    csv = "Rajasthan.csv"
elif selected_state == "Sikkim":
    csv = "Sikkim.csv"
elif selected_state == "Tamil Nadu":
    csv = "Tamil Nadu.csv"
elif selected_state == "Telangana":
    csv = "Telangana.csv"
elif selected_state == "Tripura":
    csv = "Tripura.csv"
elif selected_state == "Uttar Pradesh":
    csv = "Uttar Pradesh.csv"
elif selected_state == "Uttarakhand":
    csv = "Uttarakhand.csv"
elif selected_state == "West Bengal":
    csv = "West Bengal.csv"

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

with open('Indian_States.json') as f:
    geojson_data = json.load(f)

# Extract the boundary of the specific state you want to highlight
state_name = selectedstate.selected_state  # Replace 'Your_State_Name' with the name of the state you want to highlight
state_boundary = [feature for feature in geojson_data['features'] if feature['properties']['NAME_1'] == state_name]

map = folium.Map(location=[selected_state_lat,selected_state_long],zoom_start = 6, tiles = 'CartoDB positron',scrollWheelZoom=False)
# Add the choropleth layer with the filtered GeoJSON data
folium.Choropleth(
    geo_data={
        'type': 'FeatureCollection',
        'features': state_boundary  # Filtered GeoJSON data for the specific state
    },
    fill_color='green',  # Choose a color scale
    fill_opacity=0.7,
    line_opacity=0.2
).add_to(map)
#column layout
col1, col2, col3 = st.columns(3,gap="large")

with col1:    
    
    def calculate_spi_12_monthly(precip_data):
        spi_values = []

        # Iterate over the data to calculate SPI for each month, starting from the 13th month
        for i in range(11, len(precip_data)):
            # Extract 12 months of data for SPI calculation
            current_period_data = precip_data[i-11:i+1]

            # Step 1: Fit gamma distribution to 12-month precipitation data
            shape, loc, scale = gamma.fit(current_period_data)

            # Step 2: Calculate SPI value for the last month of the 12-month period
            spi_value = (precip_data[i] - gamma.ppf(0.5, a=shape, loc=loc, scale=scale)) / gamma.std(a=shape, loc=loc, scale=scale)

            # Append the SPI value to the list
            spi_values.append(spi_value)

        return spi_values

    # # Read precipitation data from CSV file
    precip_data = pd.read_csv(csv)

    # Extract precipitation values from 'precipitation' column
    precip_values = precip_data['Precipitation/rainfall per month'].tolist()


    # Calculate SPI12 values
    spi_12_monthly = calculate_spi_12_monthly(precip_values)

    # Add SPI12 values to the DataFrame
    precip_data['SPI12'] = [None]*11 + spi_12_monthly  # Assuming the first 12 months don't have SPI values

    # Write DataFrame with SPI12 values back to CSV file
    precip_data.to_csv('precipitation_data_with_SPI12.csv', index=False)
    st.markdown(module.translator(text="Positive SPI-12: Indicates wetter than normal conditions (less likely drought).",lang = selected_language).text)
    st.markdown(module.translator(text="    SPI-12 between 0 and -1: Near normal precipitation.",lang = selected_language).text)
    st.markdown(module.translator(text="    SPI-12 between -1.5 and -2.0: Moderately dry conditions (increased possibility of drought).",lang = selected_language).text)
    st.markdown(module.translator(text="   SPI-12 below -2.0: Severely dry conditions (strong indication of drought).",lang = selected_language).text)

with col2:
    st.markdown("## Region")

    with st.container(border=True,height=380):
        st_map = st_folium(map, width=530, height=350)
    def highlight_col(val):
        if val > -1:
            return 'background-color: lightgreen'
        elif val > -2:
            return 'background-color: yellow'
        else:
            return 'background-color: red'
    table = pd.read_csv('precipitation_data_with_SPI12.csv')
    styled_df = table.style.applymap(highlight_col, subset=['SPI12'])
    st.markdown("## Calculated SPI values")
    with st.container(border=True,height=380):
        #table = pd.read_csv('precipitation_data_with_SPI12.csv')
        st.dataframe(data=styled_df,width=500,height=350,hide_index=True)

with col3:
    st.markdown("## Predicted data for next year")
    with st.container(border=True,height=380):
        # Convert year and month columns to datetime format
        table['ds'] = pd.to_datetime(table[['Year', 'Month']].assign(day=1))
        table = table.rename(columns={'SPI12': 'y'})
        # Select only relevant columns
        df = table[['ds', 'y']]

        # 2. Create and Fit Prophet Model
        model = Prophet()
        model.fit(df)

        # 3. Make Future Predictions
        future_dates = model.make_future_dataframe(periods=12, freq='MS')  # Predicting next 12 months
        forecast = model.predict(future_dates)

        # View forecast for next year
        forecast_next_year = forecast[['ds', 'yhat']].tail(12)  # Last 12 predictions (next year)
        st.dataframe(data=forecast_next_year,height=350,width=530,hide_index=True)
    st.markdown("## Graphical view")
    with st.container(border=True,height=380):
        st.line_chart(data=forecast_next_year, x="ds", y="yhat", color="#90ee90", width=0, height=0, use_container_width=True)

drought_months = forecast_next_year[forecast_next_year['yhat'] < -1.0].shape[0]

# Calculating the total number of months
total_months = len(forecast_next_year)

# Calculate the drought occurrence percentage
drought_percentage = (drought_months / total_months) * 100

with col1:
    t1 =module.translator(text="The chances(in percentage) of occurance of drought in your region : ",lang=selected_language).text

    st.markdown(f"<p style='text-align: left;color: green;font-size: 30px;'>{t1}{drought_percentage}%</p>", unsafe_allow_html=True)
    t2 =module.translator(text="<p style = 'font-size: 20px;'>We understand the challenges farmers face, especially during dry periods. Here at Arid Insight, we're here to support you with expert tips and resources to help your farm thrive through drought:</p><p style = 'font-size: 20px;'>Water Management Warriors:</p><p> Conserve Every Drop:<br>Leak Busters: Patch those pesky leaks in your irrigation systems. A single leak can waste gallons of precious water!<br>Drip Irrigation Champions: Consider switching to drip irrigation. It delivers water directly to plant roots, minimizing evaporation.<br>Mulch Masters: Spread organic mulch around your crops. It acts like a tiny blanket, retaining soil moisture.<br>Rainwater Harvesting Heroes: Capture that skyfall! Implement rainwater harvesting techniques to store water for later use.</p><p>Crop Selection Champions:<br>Drought-Resistant Choices: Consider planting drought-resistant crops like millets, sorghum, or legumes next season. These warriors require less water and can still provide a good yield.<br>Staggered Planting Strategists: Plant crops in phases throughout the season (staggered planting). This helps distribute water needs and reduces stress on your resources.<br>Crop Scouting Detectives: Regularly monitor your crops for signs of wilting or discoloration. Early detection allows you to adjust irrigation accordingly.</p><p>Soil Health Superstars:<br>Organic Boosters: Improve soil health by adding organic matter like compost or manure. This increases the soil's water-holding capacity.<br>Tillage Tamers: Minimize tillage practices to prevent soil erosion and moisture loss. Consider alternative methods like no-till farming.</p>",lang=selected_language).text


    st.markdown(t2, unsafe_allow_html=True)
