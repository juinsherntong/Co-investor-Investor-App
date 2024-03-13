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

