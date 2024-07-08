import streamlit as st 
import pandas as pd 

def metric():
    #path to datasets(matches, players, worldcup)
    matches  = "../PortfolioOne/data/WorldCupMatches.csv"
    players  = "../PortfolioOne/data/WorldCupPlayers.csv"
    worldcup = "../PortfolioOne/data/WorldCups.csv" 
   

    matches_data = pd.read_csv(matches)
    players_data = pd.read_csv(players)
    worldcup_data = pd.read_csv(worldcup)
    #all_data= pd.read_csv(all)



    country_name = matches_data['Home Team Name']
    country_name = country_name.dropna()
    option = st.selectbox("Which team do you support ?",country_name.unique())


    col1, col2, col3,col4 = st.columns(4)
    with col1:
        st.metric('country_name',value =option)
    with col2:
        
        if option in worldcup_data['Winner'].to_list():
            winners =  worldcup_data['Winner'].to_list()
            col2option = winners.count(option)
        else:
            col2option = 0

        st.metric('Times winners',value =col2option)
    with col3:
        participationh = matches_data[matches_data['Home Team Name'] == option ]['Year']

        participationa = matches_data[matches_data['Away Team Name'] == option ]['Year']
        participation = pd.concat([participationa,participationh]).sort_values().astype(int)
        if option in  option :
            col3option = participation.nunique()
        else:
            col3option = 0

        st.metric('Participations',value =col3option)
    with col4:
        st.metric('Matches',value =len(participation))









