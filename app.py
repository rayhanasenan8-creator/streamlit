import streamlit as st
import pandas as pd
import plotly.express as px

# Load your CSV file
df = pd.read_csv("4a0321bc971cc2f793d3367fd0b55a34_20240905_102823.csv")

# Page title
st.set_page_config(page_title="Interactive Data Explorer", layout="wide")
st.title("📊 Interactive Data Explorer")

st.markdown("""
This app demonstrates **two interactive visualizations** of the dataset.  
Use the controls in the sidebar to filter and explore the data dynamically.
""")

# --- Sidebar controls ---
st.sidebar.header("🔧 Filters")

# Dropdown for choosing column to analyze
num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

col_x = st.sidebar.selectbox("Choose X-axis column:", num_cols)
col_y = st.sidebar.selectbox("Choose Y-axis column:", num_cols)

# Slider for filtering numeric values
filter_col = st.sidebar.selectbox("Filter by column:", num_cols)
min_val, max_val = df[filter_col].min(), df[filter_col].max()
selected_range = st.sidebar.slider("Select value range:", float(min_val), float(max_val), (float(min_val), float(max_val)))

# Apply filter
filtered_df = df[(df[filter_col] >= selected_range[0]) & (df[filter_col] <= selected_range[1])]

# --- Visualization 1: Scatter plot ---
st.subheader("🔵 Scatter Plot")
fig1 = px.scatter(filtered_df, x=col_x, y=col_y, color=cat_cols[0] if cat_cols else None,
                  title=f"{col_y} vs {col_x}")
st.plotly_chart(fig1, use_container_width=True)

# --- Visualization 2: Histogram ---
st.subheader("📊 Histogram")
col_hist = st.selectbox("Choose column for histogram:", num_cols)
fig2 = px.histogram(filtered_df, x=col_hist, nbins=30, title=f"Distribution of {col_hist}")
st.plotly_chart(fig2, use_container_width=True)

# Show filtered data
with st.expander("See Filtered Data Table"):
    st.write(filtered_df)
