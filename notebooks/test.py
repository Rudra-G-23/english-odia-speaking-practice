import streamlit as st
from pathlib import Path

st.write("Hello Streamlit")

BASE_DIR = Path(__file__).parent
st.write("BASE_DIR:", BASE_DIR)
