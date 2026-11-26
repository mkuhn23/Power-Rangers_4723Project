import streamlit as st

def highlight_state(states):
    selected = st.selectbox(
        "Select a state",
        states["STUSPS"]
    )

    states["highlight"] = [
        1 if state == selected else 0
        for state in states["STUSPS"]
    ]

    return states
