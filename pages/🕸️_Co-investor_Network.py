### Import libraries and packages
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from PIL import Image

### Import images
sb_title = Image.open('Sidebar title.png')
mn_title = Image.open('Main title.png')
legend = Image.open('Legend.png')

### CSS + Streamlit markdown (Edit layout and aesthetics)
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}  



</style>
'''
#-----
#____
# Correct color for dark mode
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

#------
st.markdown(hide_img_fs, unsafe_allow_html=True)

### Image in main panel (Co-investor Network Diagram)
st.image(mn_title, width=700)

### User guide expander (Main panel)
with st.expander('User Guide', expanded=False):
    st.write("First-time user? It's great to have you. Let's watch a short [tutorial video](https://drive.google.com/file/d/1SrEui4Qq-7T7k32A6UfsHZRtQpbpfEWa/view?usp=sharing) to get started :eyes:.")

### Image in sidebar (500 Data and Insights)
st.sidebar.image(sb_title, width=300)

### Company Types - Sidebar (expander)
with st.sidebar.expander('Company Type'):    
    ### Radio button to select company type to be displayed
    com_typ = st.radio('Select the 500 Global portfolio company type', 
                       ('Unicorns', 'Centaurs', 'Seed & Series A'), 
                       help="E.g. 'Unicorns' will display portfolio companies that are _unicorns_ as well as their associated co-investors in the network diagram (Source: Salesforce)")
    
    ### Import dataset's path
    if com_typ == 'Unicorns':
        path = 'Data/4. Co-investors List for Streamlit (Unicorns).csv'
    elif com_typ == 'Centaurs':
        path = 'Data/4. Co-investors List for Streamlit (Centaurs).csv'
    else:
        path = 'Data/4. Co-investors List for Streamlit (Seed and Series A).csv'
    
    ### Read and create dataframe
    slct_conn = pd.read_csv(path)

### Graph Customization (Investor) - Sidebar
### Data manipulation
### For number of co-investment slider
th = pd.DataFrame(slct_conn.groupby(['Inv_name'])['Com_name'].count())
th = th.sort_values('Com_name', ascending=False)
th.reset_index(inplace=True, level=['Inv_name'])
th = int(th['Com_name'][30:31])

minimum = int(slct_conn['No_comm'].min())
maximum = slct_conn[['No_comm']].drop_duplicates('No_comm').sort_values('No_comm').reset_index(drop=True)[-2:-1]
maximum = int(maximum['No_comm']) + 1

### For investor type dropdown
inv_type_drp = list(slct_conn['Inv_type'].drop_duplicates().sort_values())
inv_type_drp.insert(0, 'All')

### For investor's preferred industry dropdown
#pref_ind = slct_conn['Pref_industry'].str.split(', ', expand=True) # Seperate investor name by comma
#pref_ind_drp = []
#rows, columns = pref_ind.shape
#for a in range(rows): 
#    for b in pref_ind.columns:
#           if pref_ind[b][a] != None:
#                v = pref_ind[b][a]
#                pref_ind_drp.append(v)
#pref_ind_drp = sorted(list(dict.fromkeys(pref_ind_drp)))
#pref_ind_drp = [item for item in pref_ind_drp if item != '']
#pref_ind_drp.insert(0, 'All')

pref_ind_drp = list(slct_conn['Pref_industry'].str.split(', ').explode('Pref_industry').drop_duplicates().sort_values())
pref_ind_drp.insert(0, 'All')
pref_ind_drp = [item for item in pref_ind_drp if item != '']
pref_ind_drp = pref_ind_drp[0:-2]

### For investor's preferred verticals dropdown
# pref_ver = slct_conn['Pref_vertical'].str.split(', ', expand=True) # Seperate investor name by comma
# pref_ver_drp = []
# rows, columns = pref_ver.shape
# for a in range(rows): 
#    for b in pref_ver.columns:
#             if pref_ver[b][a] != None:
#                 v = pref_ver[b][a]
#                 pref_ver_drp.append(v)
# pref_ver_drp = sorted(list(dict.fromkeys(pref_ver_drp)))
# pref_ver_drp.insert(0, 'All')

pref_ver_drp = list(slct_conn['Pref_vertical'].str.split(', ').explode('Pref_vertical').drop_duplicates().sort_values())
pref_ver_drp.insert(0, 'All')
pref_ver_drp = [item for item in pref_ver_drp if item != '']
pref_ver_drp = pref_ver_drp[0:-2]


### For investor's preferred investment type dropdown
# pref_inv_type = slct_conn['Pref_inv_type'].str.split(', ', expand=True) # Seperate investor name by comma
# pref_inv_typ_drp = []
# rows, columns = pref_inv_type.shape
# for a in range(rows): 
#     for b in pref_inv_type.columns:
#             if pref_inv_type[b][a] != None:
#                 v = pref_inv_type[b][a]
#                 pref_inv_typ_drp.append(v)
# #pref_inv_typ_drp = sorted(list(dict.fromkeys(pref_inv_typ_drp)))
# pref_inv_typ_drp.insert(0, 'All')

pref_inv_typ_drp = list(slct_conn['Pref_inv_type'].str.split(', ').explode('Pref_inv_type').drop_duplicates().sort_values())
pref_inv_typ_drp.insert(0, 'All')
pref_inv_typ_drp = [item for item in pref_inv_typ_drp if item != '']
pref_inv_typ_drp = pref_inv_typ_drp[0:-2]

### Filters for Investors - Sidebar (expander)
with st.sidebar.expander('Filters for Investors'):
    no_com = st.slider('Minimum number of co-investments', 
                       minimum, maximum, th, 
                       help='E.g. a minimum number of 4 will display only co-investors that have 4 or more co-investments with 500. (Source: PitchBook and Salesforce)')
    inv_typ = st.multiselect("Investor type(s)", 
                             inv_type_drp, 
                             'All', 
                             help='Investor Types include detailed options within the broad categories of Angels/Incubators, VC, PE, Strategic Acquirers, and Others (Source: PitchBook)')
    pref_ind = st.multiselect("Investors' industry preference(s)", 
                              pref_ind_drp, 
                              'All', 
                              help="These industries follow PitchBook's taxonomy and not 500's (Source: PitchBook)")
    pref_ver = st.multiselect("Investors' vertical preference(s)", 
                              pref_ver_drp, 
                              'All', 
                              help="PitchBook verticals as defined [here](https://pitchbook.com/what-are-industry-verticals). Note that 500's portfolio company verticals (as seen in Salesforce) are more expansive. (Source: PitchBook)")
    pref_inv_type = st.multiselect("Investors' preferred deal type(s)", 
                                   pref_inv_typ_drp, 
                                   'All', 
                                   help='(Source: PitchBook)')

### Graph Customization (Portfolio Companies) - Sidebar
### Data manipulation
### For Year of initial investment
minimum = int(slct_conn['Com_ini_date'].min())
maximum = int(slct_conn['Com_ini_date'].max())
th = maximum - 3

### For PortCos's industry dropdown
com_industry_drp = list(slct_conn['Com_industry'].drop_duplicates().sort_values())
com_industry_drp.insert(0, 'All')

### For PortCos's business status dropdown
com_bus_status_drp = list(slct_conn['Com_bus_status'].drop_duplicates().sort_values())
com_bus_status_drp.insert(0, 'All')

### For PortCos's ownership status dropdown
com_own_status_drp = list(slct_conn['Com_own_status'].drop_duplicates().sort_values())
com_own_status_drp.insert(0, 'All')

### For PortCos's financing status dropdown
com_fin_status_drp = list(slct_conn['Com_fin_status'].drop_duplicates().sort_values())
com_fin_status_drp.insert(0, 'All')

### For PortCos's verticals dropdown
com_verticals = slct_conn['Com_verticals'].str.split('; ', expand=True) 
com_verticals_drp = []
rows, columns = com_verticals.shape
for a in range(rows): 
    for b in com_verticals.columns:
            if com_verticals[b][a] != None:
                v = com_verticals[b][a]
                com_verticals_drp.append(v)
com_verticals_drp = [v for v in com_verticals_drp if not(pd.isnull(v)) == True]
com_verticals_drp = sorted(list(set(com_verticals_drp)))
com_verticals_drp.insert(0, 'All')

### Filters for Portfolio Companies - Sidebar (expander)
with st.sidebar.expander('Filters for Portfolio Companies'):
    ini_inv_date = st.slider("Earliest year of 500's initial investment", 
                             minimum, maximum, th, 
                             help="E.g. if 2018 is selected, the network diagram will show all portfolio companies that 500 first invested in from 2018 and onwards (Source: Salesforce)")
    com_industry = st.multiselect("Industries", 
                                  com_industry_drp, 
                                  'All', 
                                  help="500 Global's industries (Source: Salesforce)")
    com_verticals = st.multiselect("Vertical(s)", 
                                   com_verticals_drp, 
                                   'All', 
                                   help="Verticals as seen in Salesforce based on the Data Team's Topics project (Source: Salesforce)") 
    com_bus_status = st.multiselect("Business status", 
                                    com_bus_status_drp, 
                                    'All', 
                                    help='Stage of development for a company in its lifecycle (Source: PitchBook)')
    com_own_status = st.multiselect("Ownership status", 
                                    com_own_status_drp, 
                                    'All', 
                                    help='Reflects the current ownership status of the company (Source: PitchBook)')
    com_fin_status = st.multiselect("Financing status", 
                                    com_fin_status_drp, 
                                    'All', 
                                    help='Represents the current financing status of the company - the type of investors that are backing the company (Source: PitchBook)') 
    

### Filter dataframe
if no_com == 2:
    df = slct_conn
else:
    df = slct_conn[slct_conn['No_comm'] >= no_com]
    df = df.reset_index(drop=True)
    
if 'All' in inv_typ:
    df = df
else:
    df = df[df["Inv_type"].isin(inv_typ)]
    df = df.reset_index(drop=True)
    
if 'All' in pref_ind:
    df = df
else:
    df = df[df.Pref_industry.str.contains('|'.join(pref_ind))]
    df = df.reset_index(drop=True)
    
if 'All' in pref_ver:
    df = df
else:
    df = df[df.Pref_vertical.str.contains('|'.join(pref_ver))]
    df = df.reset_index(drop=True)
    
if 'All' in pref_inv_type:
    df = df
else:
    df = df[df.Pref_inv_type.str.contains('|'.join(pref_inv_type))]
    df = df.reset_index(drop=True)

if no_com == minimum:
    df = df
else:
    df = df[df['Com_ini_date'] >= ini_inv_date]
    df = df.reset_index(drop=True)

if 'All' in com_industry:
    df = df
else:
    df = df[df["Com_industry"].isin(com_industry)]
    df = df.reset_index(drop=True)

if 'All' in com_bus_status:
    df = df
else:
    df = df[df["Com_bus_status"].isin(com_bus_status)]
    df = df.reset_index(drop=True)

if 'All' in com_own_status:
    df = df
else:
    df = df[df["Com_own_status"].isin(com_own_status)]
    df = df.reset_index(drop=True)

if 'All' in com_fin_status:
    df = df
else:
    df = df[df["Com_fin_status"].isin(com_fin_status)]
    df = df.reset_index(drop=True)

if 'All' in com_verticals:
    df = df
else:
    df = df[df.Com_verticals.str.contains('|'.join(com_verticals))]
    df = df.reset_index(drop=True)

### Company and Investor Name Search - Sidebar
### Data manipulation
### For investor name dropbown
inv_name_drp = list(df['Inv_name'].drop_duplicates().sort_values())
inv_name_drp.insert(0, 'All')

### For company name dropbown
com_name_drp = list(df['Com_name'].drop_duplicates().sort_values())
com_name_drp.insert(0, 'All')

### Company and Investor Name Search - Sidebar (expander)
### Radio button to select company or investor to be displayed
with st.sidebar.expander('Company and Investor Name Search'):
    nam_rad = st.radio('To search for a company / investor by name, first select your target', 
                       ('Company', 'Investor'))
    
    ### If user select investors
    if nam_rad == 'Investor':
        name = st.selectbox("Type an investor's name below", 
                            inv_name_drp, 
                            help='Names will auto-complete as you type (Source: PitchBook)')
        ### Filter the dataframe
        if name == 'All':
            df = df
        else:
            df = df.loc[(df.Inv_name == name)] 
            df = df.reset_index(drop=True)
    
    ### If user select companies
    else:
        name = st.selectbox("Type a company's legal name below", 
                            com_name_drp, 
                            help="Names will auto-complete as you type. Please refer to Salesforce for a company's legal name. Alternative names are not currently supported. (Source: Salesforce)")
        ### Filter the dataframe
        if name == 'All':
            df = df
        else:
            df = df.loc[(df.Com_name == name)] 
            df = df.reset_index(drop=True)

### Image in main panel (Legend)
st.image(legend, width=300)

### Network diagram creation
net = Network(height='400px', width='100%', bgcolor='#0b1e24', font_color='white') # Diagram size
G = nx.from_pandas_edgelist(df, source='Inv_name', target='Com_name') # Map the connection between Investors and Unicorns
net.add_nodes(df['Inv_name'], color=df['Inv_color'], title=df['Inv_label'], size=list(df['Inv_size'])) # Adding node to network diagram
net.add_nodes(df['Com_name'], color=df['Com_color'], size=list(df['Com_size'])) # Adding node to network diagram
net.from_nx(G) # Link NetworkX and Pyvis 
net.force_atlas_2based(gravity=-50, central_gravity=0.01, spring_length=100, spring_strength=0.08, damping=0.4, overlap=0)

try:
    path = '/tmp'
    net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
except:
    path = '/html_files'
    net.save_graph(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
 
components.html(HtmlFile.read(), height=435)       

### Import and read PitchBook data
path = 'Data/PitchBook Data for Streamlit.csv'
pd_data = pd.read_csv(path)

### Collect the list of PitchBook IDs in dataframe
slct_pd = list(df['PBID'].drop_duplicates().sort_values())

### Filter selected PitchBook IDs in PitchBook dataset
pd_data = pd_data[pd_data["Investor ID"].isin(slct_pd)]

### Convert and write new dataset
@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(pd_data)

### Download button for PitchBook data
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='coinvestors_data_from_pitchbook.csv',
    mime='text/csv')

### Footer (Last update, Description and Disclaimer)
st.caption("Last update: 4 January 2024")
st.caption("The network diagram above shows 500 Global's co-investment network (portfolio companies and co-investors). The data is sourced primarily from PitchBook, complemented with 500's internal data, as of Q4 2023. If you have questions about the app or visualization, please reach out to the Data & Insights team via the [#data](https://500global.slack.com/archives/C4HMV4AN5) Slack channel or visit the [Project KB](https://sites.google.com/500startups.com/data/initiatives-programs/038-co-investor-network?authuser=0) for more info.")
st.write("")
st.caption("DISCLAIMER: This app, network diagram, and underlying data is for 500 Global's internal use only. Please do not share information externally without going through the appropriate and relevant legal and marketing channels.")


