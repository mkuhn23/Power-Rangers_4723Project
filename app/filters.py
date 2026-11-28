import streamlit as st

def apply_filters(df):

    with st.sidebar:
        st.header("Filters")

        year = st.selectbox(
            "Year",
            ["All"] + sorted(df["year"].unique())
        )

        month = st.selectbox(
            "Month",
            ["All"] + sorted(df["month"].unique())
        )

        state = st.multiselect(
            "State",
            sorted(df["state"].unique())
        )

        producer = st.multiselect(
            "Producer Type",
            sorted(df["producer_type"].unique())
        )

        source = st.multiselect(
            "Energy Source",
            sorted(df["energy_source"].unique())
        )

    filtered = df.copy()

    if year != "All":
        filtered = filtered[filtered["year"] == year]

    if month != "All":
        filtered = filtered[filtered["month"] == month]

    if state:
        filtered = filtered[filtered["state"].isin(state)]

    if producer:
        filtered = filtered[filtered["producer_type"].isin(producer)]

    if source:
        filtered = filtered[filtered["energy_source"].isin(source)]

    return filtered
