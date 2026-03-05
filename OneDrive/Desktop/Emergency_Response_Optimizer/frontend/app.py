import streamlit as st
from dataset.dataset_loader import load_city_graph

st.title("Emergency Response System Optimizer")

city = st.text_input("Enter city", "Mumbai, India")

if st.button("Load Road Network"):

    graph = load_city_graph(city)

    st.success("Road network loaded")