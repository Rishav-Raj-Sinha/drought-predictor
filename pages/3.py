import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import module
import selectedlang

selected_language = selectedlang.selected_language


#page configs
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
hide_decoration_bar_style = '''<style>header {visibility: hidden;}
</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
#setting page background
page_bg = """
<style>
.stApp{
background-image: url("app/static/pg2.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg,unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.1,0.8,0.1])
with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<h1 style='text-align: center; color: white;'>🏜️</h1>",unsafe_allow_html=True)
    title = module.translator(text="ARID-INSIGHT",lang=selected_language).text
    st.markdown(f"<p style='text-align: center;color: white;font-size: 200px;'>{title}</p>", unsafe_allow_html=True)
    sub_heading = module.translator(text="A drought-prediction model that utilizes machine learning to predict the occurances of drought",lang=selected_language).text

    st.markdown(f"<h3 style='text-align: center; color: white;'>{sub_heading}</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    col11,col22,col33 = st.columns([0.45,0.1,0.45])
    button_title = module.translator(text="Predict",lang=selected_language).text
    with col22:
        if st.button(button_title):
            switch_page('4' )
