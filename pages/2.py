import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import selectedlang
import selectedstate
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
background-image: url("app/static/pg1.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg,unsafe_allow_html=True)

#title
title = module.translator(text="Select your state :",lang=selected_language).text

st.markdown(f"<p style='text-align: left;color: white;font-size: 40px;'>{title}</p>", unsafe_allow_html=True)

#language selector
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
selectedstate.selected_state= st.radio(
    "",
    states,
    index=None,
)
#filler
st.write("")
st.write("")
#button
if st.button('Enter site'):
            switch_page('3')
            