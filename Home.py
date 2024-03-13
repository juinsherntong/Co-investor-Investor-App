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

# .css-18ni7ap{
#     background-color: #0E1117;} 
# .css-9s5bis{
#     color: #FFFFFF;}

# .css-nigb8g{
#     color: #FFFFFF;}
# .css-fblp2m{
#     color: #FFFFFF;}   

# .css-6qob1r{
#     background-color: #262730;}
 
# .st-ds {
#     color: #FFFFFF;}
# .css-1inwz65 {
#     color: #FFFFFF;}
# .css-81oif8 {
#     color: #FFFFFF;}
# .css-1aqmucy svg {
#     fill: #FFFFFF;}
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o11 > div.css-6qob1r.e1fqkh3o3 > div.css-1vq4p4l.e1fqkh3o4 > div > div:nth-child(1) > div > div:nth-child(2) > ul > li > div.st-am.st-cd.st-ce.st-cf.st-cg > div > div:nth-child(1) > div > div > div > div > p {
#     color: #FFFFFF;}
# [role="button"] {
#     color: #FFFFFF;}
# [role="button"] {
#     border: 1px solid #505158;}
# .st-af {
#     border: 1px solid #505158;}

# .css-1x8cf1d{
#     background-color: #0E1117;
#     color: #FFFFFF;
#     border: 1px solid #FFFFFF;
#     position: absolute;
#     left: 75%;
#     border-radius: 8px;}
# .css-k1vhr4 {
#     background-color: #0E1117;}
# .css-rvekum p {
#     color: #FFFFFF;}

# .st-ew {
#     fill: black;
#     border: 1px solid #FFFFFF;}

# .css-9s5bis {
#     line-color: #FFFFFF;}

# .st-ds {
#     border: transparent;}
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o11 > div.css-6qob1r.e1fqkh3o3 > div.css-1vq4p4l.e1fqkh3o4 > div > div:nth-child(1) > div > div:nth-child(2) > ul > li > div.st-am.st-ce.st-cf.st-cg.st-ch > div > div:nth-child(1) > div > div > div {
#     color: #FFFFFF;}
# .st-gs {
#     border: transparent;}

# .css-5uatcg {
#     background-color: #0E1117;
#     color: #FFFFFF;
#     border: 1px solid #FFFFFF;
#     position: absolute;
#     left: 82%;
#     border-radius: 8px;}
    
# .st-ew {
#     border: transparent;}
# .st-fj {
#     border: transparent;}
 
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3 > div > div:nth-child(1) > div > div.css-1fcdlhc.e1s6o5jp0 > ul > li > div.st-am.st-cf.st-cg.st-ch.st-ci > div > div:nth-child(1){
#     color: #FFFFFF;}

</style>
'''


st.markdown(hide_img_fs, unsafe_allow_html=True)

### Image in main panel (Co-investor Network Diagram)
st.image(mn_title, width=700)

### User guide expander (Main panel)
with st.expander('User Guide', expanded=False):
    st.write("First-time user? It's great to have you. Let's watch a short [tutorial video](https://drive.google.com/file/d/1SrEui4Qq-7T7k32A6UfsHZRtQpbpfEWa/view?usp=sharing) to get started :eyes:.")

### Image in sidebar (500 Data and Insights)
st.sidebar.image(sb_title, width=250)

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

css=f'''
[data-testid="stSidebarNav"] {{
    position:absolute;
    bottom: 0;
    z-index: 1;
    background: {color};
}}
[data-testid="stSidebarNav"] > ul {{
    padding-top: 2rem;
}}
[data-testid="stSidebarNav"] > div {{
    position:absolute;
    top: 0;
}}
[data-testid="stSidebarNav"] > div > svg {{
    transform: rotate(180deg) !important;
}}
[data-testid="stSidebarNav"] + div {{
    overflow: scroll;
    max-height: 66vh;
}}
'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
