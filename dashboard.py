import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:Riyasa21@@localhost/fraudguardian')
df = pd.read_sql("SELECT * FROM transactions", engine)
alerts = pd.read_sql("SELECT * FROM fraud_alerts", engine)

st.title("🛡️ Fraud Detection Dashboard")
st.metric("Total Transactions", len(df))
st.metric("Fraudulent Alerts", len(alerts))
st.map(df[df['anomaly'] == 1][['location']])