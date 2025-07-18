import streamlit as st
import pandas as pd

# App config
st.set_page_config(page_title="Retail Inventory Dashboard", layout="wide")
st.title("🛒 Retail Inventory Management App")

# Load data
data = pd.read_csv("retail_store_inventory.csv")
st.write("📋 Available Columns:", data.columns.tolist())


# Show data structure
st.markdown("#### 👀 Preview Your Inventory Data")
st.dataframe(data.head(), use_container_width=True)

# Updated Inventory Summary Metrics
st.markdown("### 📊 Inventory Summary")
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(data))
col2.metric("Unique Categories", data['Category'].nunique())
col3.metric("Total Units Sold", data['Units Sold'].sum())

st.markdown("---")

# 🔽 Dropdown to filter by Region
st.subheader("🌍 Filter by Region")
region = st.selectbox("Select Region", options=["All"] + sorted(data['Region'].dropna().unique().tolist()))
filtered = data if region == "All" else data[data["Region"] == region]
st.write(f"Showing data for **{region}** region:")
st.dataframe(filtered)

st.markdown(f"📍 Showing data for **{region}** region")

# 🔍 Search Category
st.subheader("🔍 Search by Category")
search_term = st.text_input("Enter category:")
if search_term:
    results = data[data['Category'].str.contains(search_term, case=False, na=False)]
    st.write(results)

# ⚠️ Low Inventory Alert
st.subheader("⚠️ Low Inventory Alert")
inv_threshold = st.slider("Show items with Inventory Level less than:", 1, 100, 10)
if st.button("Show Low Inventory Items"):
    low_inv = data[data["Inventory Level"] < inv_threshold]
    st.warning(f"{len(low_inv)} items found below threshold of {inv_threshold}.")
    st.dataframe(low_inv)
