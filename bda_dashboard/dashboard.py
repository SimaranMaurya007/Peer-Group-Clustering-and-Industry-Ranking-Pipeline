import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Load data
# ==============================
st.title("📊 Financial Analysis Dashboard")

# Load dataset
df = pd.read_csv("analysis_outputs_full.csv")

# Drop duplicates (cik + year)
df_clean = df.drop_duplicates(subset=["cik", "year"], keep="first")

# Use cleaned dataset everywhere
st.markdown("### Dataset Information")
st.write(f"Shape before cleaning: {df.shape}")
st.write(f"Shape after cleaning: {df_clean.shape}")
st.write(f"Columns: {len(df_clean.columns)}")
st.write("Selected cluster k: **3**, silhouette score: **0.8677934635376648**")
st.write("DBSCAN clusters found: **1090** (noise = 7805)")

# ==============================
# Show clustering plots
# ==============================
st.markdown("### Clustering Visualizations")
st.image("download (3).png", caption="PCA 2D colored by KMeans (k=3)", use_container_width=True)
st.image("download (2).png", caption="PCA 2D colored by DBSCAN", use_container_width=True)
st.image("download (1).png", caption="t-SNE (sample) colored by KMeans clusters", use_container_width=True)

# ==============================
# Year selector + Top companies
# ==============================
st.markdown("### Explore Top Companies by Year")

years = sorted(df_clean["year"].dropna().unique())
selected_year = st.selectbox("Select Year", years)

df_year = df_clean[df_clean["year"] == selected_year]

# Show top companies for different metrics
st.write(f"#### Top Companies in {selected_year}")

metrics = {
    "Revenue": "revenue",
    "Profitability": "profitability_score",
    "Liquidity": "liquidity_score",
    "Leverage": "leverage_score",
    "Efficiency": "efficiency_score",
    "Growth": "growth_score",
    "Composite Score": "composite_score"
}

for label, col in metrics.items():
    if col in df_year.columns:
        top5 = df_year.nlargest(5, col)[["ticker","entity","year",col]]
        st.write(f"**Top 5 by {label}**")
        st.dataframe(top5)

st.markdown(f"### Top Companies by Revenue in {selected_year}")

if "revenue" in df_year.columns:
    top_revenue = df_year.nlargest(10, "revenue")
    st.dataframe(top_revenue[["cik","ticker","entity","year","revenue"]])
else:
    st.warning("Revenue column not found in dataset.")

# # ==============================
# # Cluster summary
# # ==============================
# st.markdown("### Cluster Summary (head)")
# st.table({
#     "Metric": ["AssetTurnover","CurrentRatio","DebtToEquity","Dividend_Yield"],
#     "Cluster 0": [5.63e5,3.10e5,2.36e7,0.0986],
#     "Cluster 1": [2.54e8,1.01,1.86e7,0.0517],
#     "Cluster 2": [0.84,1.00,2.52,0.0]
# })

st.success("Analysis complete. Outputs cleaned and ready.")
