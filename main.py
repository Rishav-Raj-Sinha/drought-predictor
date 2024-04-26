import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import selectedlang

#page configs
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
hide_decoration_bar_style = '''<style>header {visibility: hidden;}
</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
#setting page background
page_bg = """
<style>
.stApp{
background-image: url("app/static/pg1.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg,unsafe_allow_html=True)

#title
st.markdown("<p style='text-align: left;color: white;font-size: 120px;'>Welcome!</p><p style='text-align: left;color: white;font-size: 40px;'>Select your preferred language :</p>", unsafe_allow_html=True)

#language selector
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

selectedlang.selected_language = st.radio(
    "",
    official_languages_in_india,
    index=None,
)
#filler
st.write("")
st.write("")
st.write("")
#button
if st.button('Proceed'):
            switch_page('2')
            