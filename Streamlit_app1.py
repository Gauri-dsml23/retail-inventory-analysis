import streamlit as st
import pandas as pd

st.write("Available columns:", data.columns.tolist())
st.set_page_config(page_title="Retail Inventory Dashboard", layout="wide")
st.title("🛒 Retail Inventory Dashboard")

# Load data
data = pd.read_csv("retail_store_inventory.csv")

# Summary Section
st.subheader("📊 Inventory Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Items", len(data))
col2.metric("Categories", data['category'].nunique())
col3.metric("Total Quantity", data['quantity'].sum())

# Search Feature
st.subheader("🔍 Search Inventory")
search_term = st.text_input("Enter item name or keyword:")
if search_term:
    result = data[data['item_name'].str.contains(search_term, case=False, na=False)]
    st.write(result)

# Low Stock Alert
st.subheader("⚠️ Low Stock Items")
threshold = st.slider("Show items with quantity below:", 1, 50, 10)
low_stock = data[data['quantity'] < threshold]
st.write(low_stock)

# Footer
st.markdown("---")
st.caption("Made with 💙 in GitHub Codespaces | By Gauri")
