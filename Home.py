# Import libraries and packages
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from PIL import Image

# Import images
sidebar_title = Image.open('Sidebar title.png')
main_title = Image.open('Main title.png')

# CSS
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}  

.css-5uatcg {
    background-color: #0E1117;
    color: #FFFFFF;
    border: 1px solid #D2D2D2;
    position: absolute;
    left: 82%;
    border-radius: 8px;}  
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Image in main panel (Co-investor / Investor DB)
st.image(main_title, width=700)

# Image in sidebar (500 Data and Insights)
add_logo(st.sidebar.image(sidebar_title, width=300))
