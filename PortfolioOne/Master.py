import streamlit as st 
import pandas as pd 
import numpy as np
from streamlit_option_menu import option_menu
from metrics import metric

st.set_page_config(page_title='FIFA analytics',page_icon='soccer')
matches  = "../PortfolioOne/data/WorldCupMatches.csv"
players  = "../PortfolioOne/data/WorldCupPlayers.csv"
worldcup = "../PortfolioOne/data/WorldCups.csv" 


matches_data = pd.read_csv(matches)
players_data = pd.read_csv(players)
worldcup_data = pd.read_csv(worldcup)
goals_data = pd.read_csv("../PortfolioOne/data/data-csv/goals.csv" )

#Left side bar that contain web app log and navigation bar , les icon men bootstrap site 
with st.sidebar:
    st.image("./images/logo.png",width=111)
    selected = option_menu(
        "Navigation", ["players", 'matches','Tournament','FAQ'], 
        icons=['house', 'gear'],menu_icon='box-arrow-right', default_index=1),


st.header('Glory in Numbers , Data-Driven Heritage: FIFA World Cup Saga')
st.image("./images/wordcupp.png")
st.divider()

metric()

st.divider()


col1, col2 = st.columns(2)

with col1:
    year_of_competion = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]
    match_date = np.array(goals_data['match_date'])
    match_datex= [int(year) for year in pd.to_datetime(match_date).year ]
    goals_data['year'] = match_datex
    goals_data_filtered = goals_data[goals_data['year'].isin(year_of_competion)]
    goals_data_filtered.to_csv()
    goals_per_year = goals_data_filtered.groupby('year')['goal_id'].sum().reset_index()
    st.write(goals_per_year)   
    csv_filename = 'goals_per_year.csv'
    goals_data_filtered.to_csv(csv_filename, index=True) 

    st.write(type(goals_data_filtered['year']))
    match_date = list(set(goals_data_filtered['year']))== len(year_of_competion)
    st.write(match_date)