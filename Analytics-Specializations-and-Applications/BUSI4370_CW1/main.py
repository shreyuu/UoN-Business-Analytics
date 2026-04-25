# ============================================================
# ASA Coursework 1 - Customer Segmentation Pipeline
# End-to-end implementation (Python clustering required)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

RANDOM_STATE = 42

# ============================================================
# 1. LOAD DATA
# ============================================================

customers = pd.read_csv("customers_sample.csv")
category = pd.read_csv("category_spends_sample.csv")
baskets = pd.read_csv("baskets_sample.csv")
lineitems = pd.read_csv("lineitems_sample.csv")


# Convert currency columns
def parse_money(x):
    if pd.isna(x):
        return np.nan
    return float(str(x).replace("£", "").replace(",", ""))


for col in ["total_spend", "average_spend"]:
    if col in customers.columns:
        customers[col] = customers[col].apply(parse_money)

if "basket_spend" in baskets.columns:
    baskets["basket_spend"] = baskets["basket_spend"].apply(parse_money)

# Convert timestamp
baskets["purchase_time"] = pd.to_datetime(baskets["purchase_time"])

# ============================================================
# 2. FIX BAKERY ISSUE (required in Q&A)
# ============================================================

if "category" in lineitems.columns:
    lineitems["spend"] = lineitems["spend"].apply(parse_money)

    bakery_fix = (
        lineitems[lineitems["category"] == "BAKERY"]
        .groupby("customer_number")["spend"]
        .sum()
        .reset_index()
    )

    category = category.merge(
        bakery_fix, on="customer_number", how="left", suffixes=("", "_bakery_fix")
    )

    if "spend_bakery_fix" in category.columns:
        category["bakery"] = category["spend_bakery_fix"].fillna(0)
        category.drop(columns=["spend_bakery_fix"], inplace=True)

# ============================================================
# 3. FEATURE ENGINEERING (RFM + Behaviour)
# ============================================================

analysis_end = baskets["purchase_time"].max()

rfm = (
    baskets.groupby("customer_number")
    .agg(
        recency=("purchase_time", lambda x: (analysis_end - x.max()).days),
        frequency=("purchase_time", "count"),
        monetary=("basket_spend", "sum"),
        avg_basket_spend=("basket_spend", "mean"),
        avg_items=("basket_quantity", "mean"),
    )
    .reset_index()
)

# Merge with customers
features = customers.merge(rfm, on="customer_number", how="left")

# ============================================================
# 4. CATEGORY SHARE FEATURES
# ============================================================

category_cols = [c for c in category.columns if c != "customer_number"]

for col in category_cols:
    category[col] = category[col].apply(parse_money)

category["total_category_spend"] = category[category_cols].sum(axis=1)

for col in category_cols:
    category[f"share_{col}"] = category[col] / category["total_category_spend"]

share_cols = [c for c in category.columns if c.startswith("share_")]

features = features.merge(
    category[["customer_number"] + share_cols], on="customer_number", how="left"
)

features.fillna(0, inplace=True)

# ============================================================
# 5. TRANSFORM + SCALE
# ============================================================

# Log transform skewed features
for col in ["frequency", "monetary", "avg_basket_spend", "avg_items"]:
    features[col] = np.log1p(features[col])

numeric_cols = features.select_dtypes(include=np.number).columns
numeric_cols = numeric_cols.drop("customer_number")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features[numeric_cols])

# ============================================================
# 6. PCA (Dimensionality Reduction)
# ============================================================

pca = PCA(n_components=0.85, random_state=RANDOM_STATE)
X_pca = pca.fit_transform(X_scaled)

print("Number of PCA components retained:", pca.n_components_)

# ============================================================
# 7. ELBOW + SILHOUETTE (k selection)
# ============================================================

k_range = range(2, 11)
inertias = []
sil_scores = []

for k in k_range:
    km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=20)
    labels = km.fit_predict(X_pca)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_pca, labels))

# Plot elbow
plt.figure()
plt.plot(k_range, inertias, marker="o")
plt.title("Elbow Method")
plt.xlabel("k")
plt.ylabel("Inertia")
plt.savefig("elbow_plot.png", dpi=300)

# Plot silhouette
plt.figure()
plt.plot(k_range, sil_scores, marker="o")
plt.title("Silhouette Score")
plt.xlabel("k")
plt.ylabel("Score")
plt.savefig("silhouette_plot.png", dpi=300)

# ============================================================
# 8. FINAL MODEL (Choose k between 5–7)
# ============================================================

k_final = 6  # Adjust based on plots
kmeans = KMeans(n_clusters=k_final, random_state=RANDOM_STATE, n_init=20)

features["segment_id"] = kmeans.fit_predict(X_pca) + 1

# ============================================================
# 9. CLUSTER SUMMARY
# ============================================================

cluster_summary = (
    features.groupby("segment_id")
    .agg(
        n_customers=("customer_number", "count"),
        avg_frequency=("frequency", "mean"),
        avg_monetary=("monetary", "mean"),
        avg_recency=("recency", "mean"),
    )
    .reset_index()
)

cluster_summary.to_csv("cluster_summary.csv", index=False)

# ============================================================
# 10. EXPORT CUSTOMER SEGMENTS (required deliverable)
# ============================================================

features[["customer_number", "segment_id"]].to_csv("customer_segments.csv", index=False)

print("Segmentation complete.")
print(
    "Files saved: elbow_plot.png, silhouette_plot.png, cluster_summary.csv, customer_segments.csv"
)
