#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:36 2023

@author: anitabaculima
"""
import sqlite3
import pandas as pd
import streamlit as st
from sqlite3 import connect

projects = pd.read_excel("projects.xlsx")
participants = pd.read_excel("participants.xlsx")
countries = pd.read_excel("countries.xlsx")

connection = connect("ecsel_database.db")
df_projects = pd.DataFrame(projects)
df_participants = pd.DataFrame(participants)
df_countries = pd.DataFrame(countries)

df_projects.to_sql("projects", connection, if_exists = "replace")
df_participants.to_sql("participants", connection, if_exists = "replace")
df_countries.to_sql("countries", connection, if_exists = "replace")


connection.close()

# create a connection to the database
conn = sqlite3.connect('ecsel_database.db')
query = "SELECT Country, Acronym FROM countries"
df_countries = pd.read_sql(query, conn) 
conn.close()

country_dict = dict(zip(df_countries["Acronym"], df_countries["Country"]))

print(country_dict)
 
countries_option = st.selectbox('Select a Country:',df_countries["Acronym"] ) 

                        
