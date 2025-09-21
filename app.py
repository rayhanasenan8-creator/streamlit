import streamlit as st
import pandas as pd

# Load Excel file
df = pd.read_csv("4a0321bc971cc2f793d3367fd0b55a34_20240905_102823.csv") 

st.title("📊 My First Streamlit App")
st.write("Here is the data from Excel:")
st.dataframe(df)

# Add simple interaction
option = st.selectbox("Choose a column to display:", df.columns)
st.line_chart(df[option])
