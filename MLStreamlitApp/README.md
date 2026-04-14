# Machine Learning Streamlit App

## Project Overview:
An interactive web app built with Streamlit that allows users to upload their own datasets, train machine learning models, and explore how different hyperparameters affect performance.

Find the link here: https://astoquilca-may-data-science-portfolio-7rgymj8fariemmvnxzxsvm.streamlit.app/


## Features:
- Upload and explore custom datasets
- Automatic data preprocessing (encoding, imputation)
- Interactive model selection
- Real-time hyperparameter tuning
- Performance evaluation metrics
- Confusion matrix visualization
- ROC curve and AUC (binary classification only)
- Decision tree visualization
- KNN accuracy vs K analysis

## Use Instructions:
1. Upload a CSV dataset
2. Select a target column
3. The app:
    - Encodes categorical targets
    - Keeps only numeric features
    - Handles missing values using mean imputation
4. Choose a model and adjust hyperparameters
    - Logistic Regression
    - Decision Tree
    - K-Nearest Neighbors
5. View performance metrics
    - accuracy
    - precision
    - recall
    - F-1 score
    - confusion matrix
6. Explore!

## Demo:
<img width="1394" height="632" alt="Screenshot 2026-04-13 at 11 48 10 PM" src="https://github.com/user-attachments/assets/b4671a76-6bcf-4397-8c99-609eae22caed" />

## Limitations:
- Only numeric features are used (categorical features are dropped)
- No support for multi-output or advanced pipelines
- Performance may decrease with very large datasets
- Limited to basic ML models

## Installation Instructions:
1. Clone this repository
2. Install dependencies
    `pip install streamlit pandas numpy seaborn matplotlib scikit-learn`
3. Run the following command:
    `streamlit run MLstreamlit.py`
4. Then open the local URL in your browser

## References and Further Reading:
- https://www.geeksforgeeks.org/machine-learning/machine-learning-algorithms/
