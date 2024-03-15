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

# Image in main panel (Co-investor / Investor DB)
st.image(main_title, width=700)

# Image in sidebar (500 Data and Insights)
st.sidebar.image(sidebar_title, width=300)

# Read CSV file (Co-investor & Investor Database.csv)
db_data = pd.read_csv('Data/Co-investor & Investor Database.csv')

# Side bar (filters, dropdowns, etc)
inv_categories_drp = list(db_data['Investor Categories'].str.split('; ').explode('Investor Categories').drop_duplicates().sort_values())
inv_categories_drp.insert(0, 'All')
inv_categories_drp.remove('Investor')
inv_categories_drp = [item for item in inv_categories_drp if item != '']

inv_types_drp = list(db_data['Primary Investor Type'].drop_duplicates().sort_values())
inv_types_drp.insert(0, 'All')
inv_types_drp = [item for item in inv_types_drp if item != '']

HQ_country_drp = list(db_data['HQ Country/Territory'].drop_duplicates().sort_values())
HQ_country_drp.insert(0, 'All')
HQ_country_drp = [item for item in HQ_country_drp if item != '']

HQ_region_drp = list(db_data['HQ Global Region'].drop_duplicates().sort_values())
HQ_region_drp.insert(0, 'All')
HQ_region_drp = [item for item in HQ_region_drp if item != '']

with st.sidebar.expander('Filters for Investors'):
    inv_categories = st.multiselect('Investor categories',
                                    inv_categories_drp,
                                    'All',
                                    help='Investor categories...')
    inv_types = st.multiselect('Primary investor type',
                                    inv_types_drp,
                                    'All',
                                    help='Investor types...')
    HQ_country = st.multiselect('HQ countries / Territories',
                                    HQ_country_drp,
                                    'All',
                                    help='HQ countries / territories...')
    HQ_region = st.multiselect('HQ Regions',
                                    HQ_region_drp,
                                    'All',
                                    help='HQ regions...')



# Display the dataframe as output
st.dataframe(db_data)
