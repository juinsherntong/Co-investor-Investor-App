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
    # position: absolute;
    # bottom: 0%;
    # z-index: 1;
    # background: {color};
}}
# [data-testid="stSidebarNav"] > ul {{
#     padding-top: 2rem;
# }}
# [data-testid="stSidebarNav"] > div {{
#     position: absolute;
#     top: 0;
# }}
# [data-testid="stSidebarNav"] > div > svg {{
#     transform: rotate(360deg) !important;
# }}
'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown(hide_img_fs, unsafe_allow_html=True)

# Image in main panel (Co-investor / Investor DB)
st.image(main_title, width=700)

# Image in sidebar (500 Data and Insights)
st.sidebar.image(sidebar_title, width=300)

# Read CSV file (Co-investor & Investor Database.csv)
db_data = pd.read_csv('Data/Co-investor & Investor Database.csv')

# Side bar - investor demographic
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
HQ_country_drp = [item for item in HQ_country_drp if pd.notna(item)]

HQ_region_drp = list(db_data['HQ Global Region'].drop_duplicates().sort_values())
HQ_region_drp.insert(0, 'All')
HQ_region_drp = [item for item in HQ_region_drp if item != '']
HQ_region_drp = [item for item in HQ_region_drp if pd.notna(item)]

HQ_subregion_drp = list(db_data['HQ Global Sub Region'].drop_duplicates().sort_values())
HQ_subregion_drp.insert(0, 'All')
HQ_subregion_drp = [item for item in HQ_subregion_drp if item != '']
HQ_subregion_drp = [item for item in HQ_subregion_drp if pd.notna(item)]

with st.sidebar.expander('Investor Demographic'):
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
    HQ_subregion = st.multiselect('HQ Sub-regions',
                                    HQ_subregion_drp,
                                    'All',
                                    help='HQ sub-regions...')

# Side bar - investment preferences
pref_industry_drp = list(db_data['Preferred Industry'].str.split(', ').explode('Preferred Industry').drop_duplicates().sort_values())
pref_industry_drp.insert(0, 'All')
pref_industry_drp = [item for item in pref_industry_drp if item != '']
pref_industry_drp = [item for item in pref_industry_drp if pd.notna(item)]

pref_vertical_drp = list(db_data['Preferred Verticals'].str.split(', ').explode('Preferred Verticals').drop_duplicates().sort_values())
pref_vertical_drp.insert(0, 'All')
pref_vertical_drp = [item for item in pref_vertical_drp if item != '']
pref_vertical_drp = [item for item in pref_vertical_drp if pd.notna(item)]

pref_inv_type_drp = list(db_data['Preferred Investment Types'].str.split(', ').explode('Preferred Investment Types').drop_duplicates().sort_values())
pref_inv_type_drp.insert(0, 'All')
pref_inv_type_drp = [item for item in pref_inv_type_drp if item != '']
pref_inv_type_drp = [item for item in pref_inv_type_drp if pd.notna(item)]

with st.sidebar.expander('Investment Preference'):
    pref_industries = st.multiselect('Preferred industry',
                                    pref_industry_drp,
                                    'All',
                                    help='Preferred industry...')
    pref_verticals = st.multiselect('Preferred vertical',
                                    pref_vertical_drp,
                                    'All',
                                    help='Preferred verticals...')
    pref_inv_types = st.multiselect('Preferred investment types',
                                    pref_inv_type_drp,
                                    'All',
                                    help='Preferred investment types...')

# Display the dataframe as output
st.dataframe(db_data)
