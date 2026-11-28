import streamlit as st
import geopandas as gpd
import plotly.graph_objects as go
import pandas as pd
import sqlite3

# Imports from other py files
from state_highlight import highlight_state
from filters import apply_filters

# Placeholder Test
st.title("UPDATED DASHBOARD TEST")

# Connect to SQLite database
conn = sqlite3.connect("my_database.db")

# Find tables in database
tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table'",
    conn
)

# Select the energy data table
table = st.selectbox("Select Database Table", tables["name"])

# Load data from database
df = pd.read_sql_query(
    f'SELECT * FROM "{table}"',
    conn
)

conn.close()

# Apply filters to energy data
filtered_df = apply_filters(df)

# Load shapefile
states = gpd.read_file(
    "zip://Dataset and Project Descr./cb_2025_us_state_500k.zip"
)

# Remove territories
states = states[
    ~states["STUSPS"].isin(
        ["PR", "GU", "VI", "AS", "MP"]
    )
].copy()

states = states.to_crs("EPSG:4326")

# Highlight selected state
states = highlight_state(states)

# Create interactive map
fig = go.Figure(
    data=go.Choropleth(
        locations=states["STUSPS"].tolist(),
        locationmode="USA-states",
        z=states["highlight"].tolist(),
        zmin=0,
        zmax=1,
        text=states["NAME"].tolist(),
        colorscale=[
            [0, "lightblue"],
            [0.499, "lightblue"],
            [0.5, "orange"],
            [1, "orange"]
        ],
        showscale=False,
        marker_line_color="black",
        marker_line_width=0.5
    )
)

fig.update_geos(
    scope="usa",
    projection_type="albers usa"
)

fig.update_layout(
    title="Power Rangers - US Energy Map",
    height=600,
    margin=dict(l=0, r=0, t=50, b=0)
)

# Display map in Streamlit
st.plotly_chart(fig, width="stretch")

# Display filtered energy data
st.subheader("Filtered Energy Data")
st.dataframe(filtered_df)
