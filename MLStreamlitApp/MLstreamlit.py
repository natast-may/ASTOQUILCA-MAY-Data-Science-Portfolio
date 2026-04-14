# =========================
# imports
# =========================

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_curve,
    auc,
    classification_report,
    mean_squared_error,
    r2_score
)

from sklearn import tree


# =========================
# page setup
# =========================

st.set_page_config(page_title="ML Exploration App", layout="wide")

st.title("Machine Learning Explorer")

st.write(
    "Upload a dataset, choose a model, and explore how hyperparameters affect performance!"
)

st.markdown("---")


# =========================
# upload data
# =========================

st.header("🍎 Upload Your Dataset")

uploaded_file = st.file_uploader("Drop your CSV here ⬇️", type=["csv"])

if uploaded_file is None:
    st.info("Please upload a dataset to begin.")
    st.stop()

# load dataset
df = pd.read_csv(uploaded_file)

st.subheader("Preview")
st.dataframe(df.head())


# =========================
# dataset overview
# =========================
st.markdown("---")
st.header("🍎 Dataset Overview")

st.write("Summary Statistics")
st.write(df.describe())

# =========================
# target selection
# =========================

st.sidebar.header("1. Select Target Column")

target = st.sidebar.selectbox("Target Column", df.columns)


# =========================
# data preprocessing
# =========================

X = df.drop(columns=[target])
y = df[target]

# encode target if categorical
if y.dtype == "object":
    le = LabelEncoder()
    y = le.fit_transform(y)

# keep only numeric features
X = X.select_dtypes(include=["number"])

if X.shape[1] == 0:
    st.error("No numeric features found. Please use a dataset with numeric columns :)")
    st.stop()

# for missing vlaues, we will impute with mean 
imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

# =========================
# model selection
# =========================

st.sidebar.header("2. Choose Model")

model_option = st.sidebar.selectbox(
    "Model",
    ["Logistic Regression", "Decision Tree", "K-Nearest Neighbors"]
)


# =========================
# model descriptions
# descriptions adapted from https://www.geeksforgeeks.org/
# =========================
st.markdown("---")
if model_option == "Logistic Regression":
    st.success("**Logistic Regression** is a supervised machine learning algorithm used for classification problems. It predicts the probability that an input belongs to a specific class.")

elif model_option == "Decision Tree":
    st.success("**Decision Tree** is a supervised machine learning algorithm used for both classification and regression tasks.")

elif model_option == "K-Nearest Neighbors":
    st.success("**K-Nearest Neighbors** is a (weakly) supervised machine learning technique for classification and regression tasks. It works by identifying the K closest data points to a given input and making predictions based on the majority class or average value of those neighbors")

# =========================
# hyperparameters
# =========================

st.sidebar.header("3. Hyperparameters")

test_size = st.sidebar.slider("Test Size", 0.1, 0.4, 0.2)

if model_option == "Decision Tree":
    max_depth = st.sidebar.slider("Max Depth", 1, 20, 5)

if model_option == "K-Nearest Neighbors":
    k = st.sidebar.slider("K (Neighbors)", 1, 15, 5)


# =========================
# train-test split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42
)


# =========================
# model setup
# =========================

if model_option == "Logistic Regression":
    model = LogisticRegression(max_iter=1000)

elif model_option == "Decision Tree":
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)

elif model_option == "K-Nearest Neighbors":
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=k)


# =========================
# training
# =========================

model.fit(X_train, y_train)
y_pred = model.predict(X_test)


# =========================
# results section
# =========================

st.header("🍎 Model Results")

accuracy = accuracy_score(y_test, y_pred)


st.subheader("Performance Metrics")
st.metric("Accuracy", round(accuracy, 2))

st.text("Classification Report")
st.text(classification_report(y_test, y_pred))

st.subheader("Notes on Metrics")
st.write("**Accuracy** measures overall correctness.")
st.write("**Precision** measures the proportion of true positive predictions among all positive predictions.")
st.write("**Recall** measures the proportion of true positive predictions among all actual positive instances.")
st.write("**F1-Score** is the harmonic mean of precision and recall.")

st.subheader("Confusion Matrix")
st.write("The confusion matrix shows the counts of true positives, true negatives, false positives, and false negatives.")
cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
st.pyplot(fig)


# =========================
# ROC CURVE (binary only)
# =========================

if len(np.unique(y)) == 2 and hasattr(model, "predict_proba"):

    st.subheader("ROC Curve & AUC")
    st.write("The ROC curve plots the true positive rate against the false positive rate at various threshold settings. The AUC (Area Under the Curve) summarizes the overall performance of the model.")

    y_prob = model.predict_proba(X_test)[:, 1]

    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    st.metric("AUC", round(roc_auc, 2))

    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    ax.plot([0, 1], [0, 1], "--")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend()

    st.pyplot(fig)


# =========================
# decision tree visualization
# =========================

if model_option == "Decision Tree":
    st.subheader("Decision Tree Visualization")

    try:
        dot_data = tree.export_graphviz(
            model,
            feature_names=X.columns,
            class_names=[str(c) for c in np.unique(y)],
            filled=True
        )

        st.graphviz_chart(dot_data)

    except:
        st.warning("Could not render decision tree visualization Keep max depth low for better visualization!")


# =========================
# KNN analysis plot
# =========================

if model_option == "K-Nearest Neighbors":

    st.subheader("K vs Accuracy Analysis")

    k_values = range(1, 20, 2)
    accuracies = []

    scaler_knn = StandardScaler()
    X_train_knn = scaler_knn.fit_transform(df[X.columns])
    X_test_knn = scaler_knn.transform(df[X.columns])

    for k_temp in k_values:
        knn = KNeighborsClassifier(n_neighbors=k_temp)
        knn.fit(X_train, y_train)
        pred = knn.predict(X_test)
        accuracies.append(accuracy_score(y_test, pred))

    fig, ax = plt.subplots()
    ax.plot(k_values, accuracies, marker="o")
    ax.set_xlabel("K")
    ax.set_ylabel("Accuracy")
    ax.set_title("KNN Performance vs K")

    st.pyplot(fig)


# =========================
# footer
# =========================

st.markdown("---")
st.markdown(
    """
4.13.26 - ML Explorer App by Natalie Astoquilca-May
"""
)