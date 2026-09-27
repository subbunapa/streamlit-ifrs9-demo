# streamlit-ifrs9-demo

IFRS9 Stage Checker (Streamlit Demo)

A simple Streamlit app that checks IFRS9 staging (Stage 1/2/3) based on Days Past Due, using basic rule-based logic. Built as a first hands-on project to learn Streamlit.

Live Demo

[Add your Streamlit Cloud link here once deployed]

Run Locally
pip install -r requirements.txt
streamlit run app.py
How it works

Enter a customer's Days Past Due, click "Check Stage", and the app applies simple IFRS9 staging rules:

0–29 days → Stage 1 (Performing)
30–89 days → Stage 2 (Significant Increase in Credit Risk)
90+ days → Stage 3 (Credit-Impaired / Default)
