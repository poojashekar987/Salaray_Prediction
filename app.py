import streamlit as st
from predict_view import show_predict_view
from explore_view import show_explore_view


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_view()
else:
    show_explore_view()