# importing all the necessary libraries for the app
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# Page configuration (title and layout)
st.set_page_config(page_title="World Happiness ML", layout="wide")

st.title("🌷 World Happiness Report: ML Analysis")
st.write(
    "Utilize the 2026 World Happiness dataset, choose a machine learning method, "
    "and see how countries group together naturally based on their statistics!"
)

# ── 1. DATASET SELECTION & UPLOAD ──────────────────────────────────────────────
st.sidebar.header("1. Dataset")

# sidebar section
# Lets the user choose between the built-in dataset or uploading their own
data_source = st.sidebar.radio(
    "Choose your data source:",
    ["World Happiness Report", "Upload your own CSV"]
)
#caching the data helps keep the app fast and prevents reloading the dataset every time the user changes a setting.
@st.cache_data
def load_built_in():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "world_happiness.csv") # finding absolute path to avoid issues locating the csv
    return pd.read_csv(file_path)

raw_df = None
# adding the WHR as a built-in option. 
if data_source == "World Happiness Report":
    try:
        raw_df = load_built_in()
        st.sidebar.success("🌷 World Happiness Report loaded.")
    except FileNotFoundError:
        st.error("❕❕ File not found! Is the 'world_happiness.csv' file in the same directory as this app?")
        st.stop()
else:
    # Handle custom user uploads (must be a csv)
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        raw_df = pd.read_csv(uploaded_file)
        st.sidebar.success("✅ Custom dataset loaded.")
    else:
        st.info("Please upload a CSV file in the sidebar to begin your analysis.")
        st.stop() # Stops the rest of the app from running until a file is provided!!!

# ── 2. DATA CLEANING & INDEXING ───────────────────────────────────────────────
df = raw_df.copy() # making a working copy ensures that we don't accidentally modify the original data.


# Provide a dropdown for the index column
# also helps ensure that custom datasets don't crash the app
st.sidebar.subheader("Row Labels (Optional)")
index_options = ["None"] + df.columns.tolist()

# Try to default to "Country name" or "Country" if it exists, otherwise default to "None"
default_index = "None"
if "Country name" in df.columns:
    default_index = "Country name"
elif "Country" in df.columns:
    default_index = "Country"

index_col = st.sidebar.selectbox(
    "Select a column to use as the label/index:",
    options=index_options,
    index=index_options.index(default_index)
)

if index_col != "None":
    df.set_index(index_col, inplace=True)

# Cleaning: Convert any text columns to numbers, then drop missing values
for col in df.select_dtypes(include=["object", "category"]).columns:
    df[col] = df[col].astype("category").cat.codes
df = df.dropna()

# Show preview and current data source at the top of the app
st.header("🌼 Dataset Preview")
st.write(f"Currently analyzing: **{data_source}**")
st.dataframe(df.head())

# ── 3. FEATURE SELECTION ───────────────────────────────────────────────────────
#sidebar for selecting which features/columns to include in the analysis. 
st.sidebar.header("2. Select Features")
selected_cols = st.sidebar.multiselect(
    "Columns to include:",
    options=df.columns.tolist(),
    default=df.columns.tolist()
)

# users must select at least 2 for clustering or PCA to run. 
if len(selected_cols) < 2:
    st.error("❕❕ Please select at least 2 columns to continue!")
    st.stop()
# a subset of the data with only the selected features is used for analysis.
df_selected = df[selected_cols]

# ── 4. SCALING (PREPROCESSING) ─────────────────────────────────────────────────
# Standardizing the data so big numbers don't overpower small numbers
scaler = StandardScaler()
X = scaler.fit_transform(df_selected)
#storing features to use later in the PCA table.
feature_names = df_selected.columns.tolist()

# ── 5. CHOOSE METHOD ───────────────────────────────────────────────────────────
# sidebar allows user to choose ML method.
st.sidebar.header("3. Choose Method")
method = st.sidebar.radio(
    "Select an algorithm:",
    ["K-Means Clustering", "Hierarchical Clustering", "PCA"]
)
# main results section header
st.divider()
st.header("🌸 Results")

# ── K-MEANS ────────────────────────────────────────────────────────────────────
if method == "K-Means Clustering":
    k = st.sidebar.slider("Number of clusters (k)", 2, 10, 3) # slider for choose number of clusters
    
    # Run the model (initialize and fit)
    kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
    labels = kmeans.fit_predict(X) # predict cluster labels for each data point (country)
    
    # Metrics
    col1, col2 = st.columns(2) # two columns to display metrics side by side
    col1.metric("Clusters (k)", k) 
    col1.write("The number of clusters controls how many groups the model creates.")
    col2.metric("Silhouette Score", round(silhouette_score(X, labels), 3))
    col2.write("The silhouette score ranges from -1 to 1, with values closer to 1 indicating better-defined clusters.")
    st.divider()

    # Visual 1: Elbow Plot
    # will help show the right numbers of clusters.
    st.subheader("Elbow Plot")
    st.write("Look for the elbow to find the best number of clusters.")
    
    # running k-means for a range of k values to calculate inertia 
    # inertia is the sum of squared distances of samples to their closest cluster center.
    inertias = []
    k_range = range(2, 11)
    for ki in k_range:
        m = KMeans(n_clusters=ki, random_state=42, n_init="auto").fit(X)
        inertias.append(m.inertia_)

    # plotting elbow plot using matplotlib
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(list(k_range), inertias, marker='o') # (inertia vs k)
    ax.set_xlabel("Number of Clusters (k)")
    ax.set_ylabel("Inertia")
    st.pyplot(fig)

    st.divider()

    # Visual 2: Cluster Averages Table
    st.subheader("Cluster Profile Table")
    st.write("This table shows the average value of each selected variable within each cluster.")
    st.write("It can be helpful to explore each cluster's characteristics and understand what differentiates them.")
    
    # adding the cluster labels to the original selected dataframe 
    # grouping by cluster to show average values for each feature in each cluster.
    df_labeled = df_selected.copy()
    df_labeled["Cluster"] = labels
    st.dataframe(df_labeled.groupby("Cluster").mean().round(2))


# ── HIERARCHICAL CLUSTERING ────────────────────────────────────────────────────
elif method == "Hierarchical Clustering":
    n_clusters = st.sidebar.slider("Number of clusters", 2, 10, 3) # slider for number of clusters
    linkage_method = st.sidebar.selectbox("Linkage method", ["ward", "complete", "average"]) 
    st.sidebar.write("The linkage method controls how distances between groups are calculated.")
    st.sidebar.write("**Ward** often creates compact clusters. **Complete** and **average** can capture more complex relationships but may be more sensitive to outliers.")
    # linkage method determines how the distance between clusters is calculated when merging them in the hierarchical clustering process.
    
    # Run the model
    # initializing and fitting the AC model to the data.
    # The fit_predict method computes cluster labels for each data point.
    hier = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage_method)
    labels = hier.fit_predict(X)
    
    # Metrics and display
    col1, col2 = st.columns(2)
    col1.metric("Clusters", n_clusters)
    col1.write("The number of clusters controls how many groups the model creates.")
    col2.metric("Silhouette Score", round(silhouette_score(X, labels), 3))
    col2.write("The silhouette score ranges from -1 to 1, with values closer to 1 indicating better-defined clusters.")

    st.divider()

    # Visual 1: Dendrogram
    st.subheader("Dendrogram (The Clustering Tree)")
    st.write("This tree shows how individual data points are merged into larger groups. Explore this to find natural clusters in the data.")
    
    Z = linkage(X, method=linkage_method)
    fig, ax = plt.subplots(figsize=(10, 5))
    
    #plot dendrogram using scipy's dendrogram function:
    dendrogram(
        Z, ax=ax, truncate_mode="lastp", p=30, #only show the last 30 merges for readability
        labels=df.index.tolist(), leaf_rotation=45, leaf_font_size=9 #rotate labels for better visibility
    )
    ax.set_ylabel("Distance")
    st.pyplot(fig)

    st.divider()

    # Visual 2: Cluster Averages Table
    # same strategy as k-means
    #  adding cluster labels to original df and grouping by cluster
    st.subheader("Cluster Averages")
    st.write("This table shows the average value of each selected variable within each cluster.")
    df_labeled = df_selected.copy()
    df_labeled["Cluster"] = labels
    st.dataframe(df_labeled.groupby("Cluster").mean().round(2))


# ── PCA ────────────────────────────────────────────────────────────────────────
elif method == "PCA":
    n_components = st.sidebar.slider("Number of components", 2, min(5, len(feature_names)), 2) #slider for choosing number of principal components.
    st.sidebar.write("This controls how many new dimensions the model creates to represent the data. More components capture more variance but can be harder to visualize and interpret.")
    
    # Run the model (fit and transform)
    pca = PCA(n_components=n_components, random_state=42)
    X_pca = pca.fit_transform(X)
    
    total_var = pca.explained_variance_ratio_.sum() # total variance captured by the selected components
    st.metric(f"Total Variance Captured by {n_components} Components", f"{total_var:.1%}") #display
    st.write("This metric shows how much of the original data's variance is captured by the selected principal components. A higher percentage means the components are doing a better job of representing the original data.")

    st.divider()

    # Visual 1: Variance Explained Bar Chart
    st.subheader("Variance by Component")
    st.write("Use this bar chart to compare the amount of variance explained by each principal component, and decide how many to include.")
    evr = pca.explained_variance_ratio_
    
    #bar chart showing how much variance each principal component captures from the original data.
    fig, ax = plt.subplots(figsize=(6, 4)) 
    ax.bar([f"PC{i+1}" for i in range(len(evr))], evr)
    ax.set_ylabel("Explained Variance Ratio")
    st.pyplot(fig)

    st.divider()

    # Visual 2: 2D Scatter Plot
    st.subheader("2D PCA Scatter Plot")
    st.write("Viewing the data using the top two principal components.")
    
    # scatter plot of the data points in the space defined by the first two principal components.
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7) 
    ax.set_xlabel(f"PC1 ({evr[0]:.1%} variance)")
    ax.set_ylabel(f"PC2 ({evr[1]:.1%} variance)")
    st.pyplot(fig)

    st.divider()

    # Visual 3: Loadings Table
    st.subheader("Component Loadings")
    st.write("This table shows which original features heavily influence each component.")
    
    # The loadings indicate how much each original feature contributes to each principal component.
    loadings = pd.DataFrame(
        pca.components_.T,
        index=feature_names,
        columns=[f"PC{i+1}" for i in range(n_components)]
    ).round(3)
    st.dataframe(loadings)
