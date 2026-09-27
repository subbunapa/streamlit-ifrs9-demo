"""
app.py — a minimal Streamlit app to learn the basics.

No LLM, no RAG here on purpose — just Streamlit's core building blocks:
a title, an input widget, a button, and displaying output.
Run with: streamlit run app.py
"""

import streamlit as st

st.title("IFRS9 Stage Checker (Simple Rules)")

st.write("Enter a customer's days past due to see which IFRS9 stage applies.")

days_past_due = st.number_input("Days Past Due", min_value=0, max_value=365, value=0)

if st.button("Check Stage"):
    if days_past_due < 30:
        stage = "Stage 1 — Performing"
    elif days_past_due < 90:
        stage = "Stage 2 — Significant Increase in Credit Risk"
    else:
        stage = "Stage 3 — Credit-Impaired / Default"

    st.success(f"Result: {stage}")
