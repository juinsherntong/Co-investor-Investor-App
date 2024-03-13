import streamlit as st

### Import images
sb_title = Image.open('Sidebar title.png')
mn_title = Image.open('Main title.png')
legend = Image.open('Legend.png')

st.set_page_config(
  page_title = 'Multipages App'
)

st.title('Home page')
st.sidebar.success('Select a page below')
