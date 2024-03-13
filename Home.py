import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from PIL import Image

st.set_page_config(
  page_title = 'Multipages App'
)

# st.sidebar.success('Select a page below')
st.title('Home page')

### Import images
sb_title = Image.open('Sidebar title.png')
mn_title = Image.open('Main title.png')
legend = Image.open('Legend.png')

st.markdown(hide_img_fs, unsafe_allow_html=True)

### Image in main panel (Co-investor Network Diagram)
st.image(sb_title, width=700)
