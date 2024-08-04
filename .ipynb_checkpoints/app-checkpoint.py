import streamlit as st
import pandas as pd

st.sidebar.radio(
    'Select an Option',
    ('Modal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)