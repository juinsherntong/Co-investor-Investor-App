import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from PIL import Image

st.set_page_config(
  page_title = 'Multipages App'
)

### Import images
sb_title = Image.open('Sidebar title.png')
mn_title = Image.open('Main title.png')

### CSS + Streamlit markdown (Edit layout and aesthetics)
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}  
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

### Image in main panel (Co-investor Network Diagram)
st.image(mn_title, width=700)

### Image in sidebar (500 Data and Insights)
st.sidebar.image(sb_title, width=300)

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css?family=Playfair Display' rel='stylesheet');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""

st.markdown(streamlit_style, unsafe_allow_html=True)

#____
# Correct color for dark mode
color = '#262730'

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
# [data-testid="stSidebarNav"] > div {{
#     position: absolute;
#     top: 0;
# }}
# [data-testid="stSidebarNav"] > div > svg {{
#     transform: rotate(180deg) !important;
# }}
# [data-testid="stSidebarNav"] + div {{
#     overflow: scroll;
#     max-height: 66vh;
# }}
# #logo {{
#     overflow: hidden !important;  /* or overflow: auto !important; depending on your preference */
}}
'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
