### Import Libraries 
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

### Import Data
unicorns = pd.read_csv(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\Files\FinalUnicorns.csv')
cities = pd.read_csv(r'C:\Users\frans\Documents\GitHub\Project4-WebScrap\Files\FinalCities.csv')

### Set Page Format
st.set_page_config(page_title='NomadVsUnicorns', page_icon=None, layout='wide', menu_items=None)