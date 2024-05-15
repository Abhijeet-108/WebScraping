import streamlit as st
import plotly.express as px
import sqlite3

st.title("Graph of Data using WebScraping")

connection = sqlite3.connect("temp.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temperatures")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temp FROM temperatures")
temp = cursor.fetchall()
temp = [item[0] for item in temp]

figure = px.line(x=date, y=temp, labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)