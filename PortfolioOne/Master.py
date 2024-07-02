import streamlit as st 
import pandas as pd 
from streamlit_option_menu import option_menu
from metrics import metric

st.set_page_config(page_title='FIFA analytics',page_icon='soccer')
matches  = "../PortfolioOne/data/WorldCupMatches.csv"
players  = "../PortfolioOne/data/WorldCupPlayers.csv"
worldcup = "../PortfolioOne/data/WorldCups.csv" 


matches_data = pd.read_csv(matches)
players_data = pd.read_csv(players)
worldcup_data = pd.read_csv(worldcup)

#Left side bar that contain web app log and navigation bar , les icon men bootstrap site 
with st.sidebar:
    st.image("./images/logo.png",width=111)
    selected = option_menu(
        "Navigation", ["players", 'Games','FAQ'], 
        icons=['house', 'gear'],menu_icon='box-arrow-right', default_index=1),


st.header('Glory in Numbers , Data-Driven Heritage: FIFA World Cup Saga')
st.image("./images/wordcupp.png")
st.divider()

metric()

st.divider()

#Filter by Year to see some summary stats
matches_data= matches_data['Year'].dropna()
years_int = [int(year) for year in matches_data]

option = st.multiselect("Select",list(set(years_int)))



