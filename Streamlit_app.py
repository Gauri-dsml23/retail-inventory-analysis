import streamlit as st
import pandas as pd

st.title("🛒 Retail Inventory Dashboard")

data = pd.read_csv("retail_store_inventory.csv")
st.write("### Sample Inventory Data", data.head())

st.write("### Total Items in Stock")
st.metric(label="Items", value=len(data))
