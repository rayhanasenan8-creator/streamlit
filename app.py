import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("4a0321bc971cc2f793d3367fd0b55a34_20240905_102823.csv")

# Page settings
st.set_page_config(page_title="Interactive Data Insights", layout="wide")
st.title("📊 Interactive Data Insights Dashboard")

st.markdown("""
Welcome to this **interactive dashboard**!  
Here you will explore the dataset through two related visualizations:
1. A **scatter plot** that shows the relationship between two numerical columns.  
2. A **histogram** that shows the distribution of a chosen variable.  

Use the controls in the sidebar to interact with the data.
""")

# Sidebar filters
st.sidebar.header("🔧 Filters")
num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

col_x = st.sidebar.selectbox("Choose X-axis (scatter):", num_cols)
col_y = st.sidebar.selectbox("Choose Y-axis (scatter):", num_cols)

filter_col = st.sidebar.selectbox("Filter data by column:", num_cols)
min_val, max_val = df[filter_col].min(), df[filter_col].max()
selected_range = st.sidebar.slider("Select value range:", float(min_val), float(max_val), (float(min_val), float(max_val)))

filtered_df = df[(df[filter_col] >= selected_range[0]) & (df[filter_col] <= selected_range[1])]

# Visualization 1: Scatter plot
st.header("🔵 Scatter Plot: Relationship Analysis")
fig1 = px.scatter(filtered_df, x=col_x, y=col_y, color=cat_cols[0] if cat_cols else None,
                  title=f"{col_y} vs {col_x}")
st.plotly_chart(fig1, use_container_width=True)

st.markdown(f"""
**Insight:**  
This scatter plot shows the relationship between **{col_x}** and **{col_y}**.  
By applying the filter on **{filter_col}**, we can focus on a specific range and see how the variables interact in that subset of the data.
""")

# Visualization 2: Histogram
st.header("📊 Histogram: Distribution Analysis")
col_hist = st.selectbox("Choose column for histogram:", num_cols)
fig2 = px.histogram(filtered_df, x=col_hist, nbins=30, title=f"Distribution of {col_hist}")
st.plotly_chart(fig2, use_container_width=True)

st.markdown(f"""
**Insight:**  
The histogram shows the distribution of **{col_hist}** across the dataset.  
Filtering the dataset helps us understand how the distribution shifts when focusing only on certain ranges of **{filter_col}**.
""")

# Data table
with st.expander("🔍 View Filtered Data Table"):
    st.write(filtered_df)
