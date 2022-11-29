import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.markdown("<h1 style='text-align: center; color: black;'>Meet Our Team</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Innovation For The Better</h2>", unsafe_allow_html=True)




image = Image.open( "111.png")
st.image(image, width= 950)




image = Image.open( "z.jpg")
st.image(image, width= 700)

st.header("Rahul: Our goal is to utilize machine learning to create an accurate prediction for users")
st.header("Shubh: We want a up to date application that decreases property damages")
st.header("Adarsh: Our group has worked continuously to provide a crucial webpage for predicting property damage.")
st.header("James: We used extensive data to provide accurate results with methodology to achieve accurate results")






