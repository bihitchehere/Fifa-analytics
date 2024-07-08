import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 


data = pd.read_csv("../PortfolioOne/data/goals_per_year.csv")
goals_per_year  = np.array(data.groupby("year")["goal_id"].count().reset_index())
goals_per_match = np.array(data.groupby("match_id")["goal_id"].count().reset_index())


fig1 = px.line(goals_per_year,x=0,y=1,title="goals dyale borzok")
fig2= px.line(goals_per_match[:5],x=0,y=1,title="goals dyale borzok")
fig1.update_traces(line=dict(color='red'))
fig2.update_traces(line=dict(color='orange'))
figure = go.Figure(data=fig1.data + fig2.data)
figure.show()




