import streamlit as st
import geopandas as gpd
import plotly.graph_objects as go

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

# Create interactive map
fig = go.Figure(
    data=go.Choropleth(
        locations=states["STUSPS"].tolist(),
        locationmode="USA-states",
        z=[1] * len(states),
        text=states["NAME"].tolist(),
        colorscale="Blues",
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
st.plotly_chart(fig, use_container_width=True)
