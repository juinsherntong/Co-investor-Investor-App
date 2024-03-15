# Import libraries and packages
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from PIL import Image

# Import images
sb_title = Image.open('Sidebar title.png')
mn_title = Image.open('Main title.png')

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

color = '' #'#262730'

css = f'''
[data-testid="stSidebarNav"] {{
    position: absolute;
    bottom: 0;
    z-index: 1;
    background: {color};
}}
[data-testid="stSidebarNav"] > ul {{
    padding-top: 2rem;
}}
[data-testid="stSidebarNav"] > div {{
    position: absolute;
    top: 0;
}}
[data-testid="stSidebarNav"] > div > svg {{
    transform: rotate(180deg) !important;
}}
'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown(hide_img_fs, unsafe_allow_html=True)

### Image in main panel (Co-investor Network Diagram)
st.image(mn_title, width=700)

### Image in sidebar (500 Data and Insights)
st.sidebar.image(sb_title, width=300)

db_data = pd.read_csv('Data/Co-investor & Investor Database.csv')
print(db_data)
