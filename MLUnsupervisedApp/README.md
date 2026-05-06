# Machine Learning Unsupervised Streamlit App
## Project Overview:
This project is an interactive Streamlit web application designed to explore unsupervised machine learning techniques such as k-means clustering, hierarchical clustering, and principal component analysis (PCA). Users can experiment with the built-in World Happiness Report dataset, or upload their own custom tabular data to discover hidden patterns, groupings, and underlying structures without the need for labeled target variables.

🌷 Find the live app here: [World Happiness Report: ML Analysis](https://astoquilca-may-data-science-portfolio-gcxqprhsaw63tymv83ghx2.streamlit.app/)

## Features:
- **Dynamic Data Processing:** Includes automatic feature selection, custom row-indexing, and standard scaling to ensure reliable model performance.
- **K-Means Clustering:** Interactive selection of k clusters, featuring live silhouette scores, cluster average tables, and an Elbow Plot to help determine the optimal number of groupings.
     - 📍*K-means clustering is a distance-based algorithm that groups data into distinct subgroups by assigning data points to their nearest cluster center.* 
- **Hierarchical Clustering:** Tune the number of clusters and linkage methods (ward, complete, average) while visualizing the merging process through an interactive Dendrogram.
     - 📍*Hierarchical clustering is a bottom-up algorithm that builds a hierarchy or "tree" of clusters by merging the most similar, closely related data points together.*
- **Principal Component Analysis (PCA):** Reduce dataset dimensionality and visualize variance through 2D scatter plots and component loading tables.
     - 📍*PCA is a dimensionality reduction technique that transforms large datasets into a smaller set of summary variables (principal components) while preserving as much of the original information as possible.*
## Use Instructions:
1. Select a data source
     - On the left sidebar, choose to use the pre-loaded World Happiness Report or upload your own CSV file with at least 2 numeric columns
2. Configure data
      - (If uploading a custom CSV) Select a column to act as your row index/label to ensure it isn't treated as a numeric feature.
3. Select features
     - Use the multiselect tool to choose which numeric columns you want the algorithms to analyze. (You must select at least two).
4. Choose an algorithm
     - Select between K-Means, Hierarchical Clustering, or PCA.
5. Tune hyperparameters
     - Use the sliders and dropdowns to adjust settings like the number of clusters, components, or linkage types.
6. Analyze results and explore!
     - Observe how your parameter changes immediately update the charts, metrics, and data tables on the main screen.

## Demo Images:
<img width="1470" height="956" alt="Screenshot 2026-05-05 at 8 17 33 PM" src="https://github.com/user-attachments/assets/73567ddb-f318-409a-98c1-9fea05925165" />
<img width="525" height="505" alt="wlbow" src="https://github.com/user-attachments/assets/18237106-3bbe-4f0f-a639-17d8798cf76a" />
<img width="781" height="586" alt="scatplot" src="https://github.com/user-attachments/assets/6c27a1e3-7e5a-422c-9049-a25a131b47fc" />
<img width="781" height="497" alt="dendy" src="https://github.com/user-attachments/assets/9629f160-62bc-4c2c-b699-853c2adfa5a8" />

## Dataset Description:
The [built-in dataset](https://www.kaggle.com/datasets/hassanali789/world-happiness-report-2026-official-rankings) provides the complete country-level rankings and happiness scores from the [World Happiness Report 2026](https://www.worldhappiness.report/ed/2026/) — the most recent edition, published March 20, 2026. It covers 147 countries across all major world regions. 

Country happiness scores are based on the Cantril Ladder question, which asks respondents to rate their current life on a scale from 0 (worst possible life) to 10 (best possible life). The 2026 scores represent a three-year average of responses collected between 2023 and 2025, covering 147 countries.

| column name             | meaning                                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| rank                    | Happiness ranking: 1 = happiest country                                                                |
| country                 | Country name                                                                                           |
| region                  | World region (e.g. Western Europe, Sub-Saharan Africa)                                                 |
| score                   | Happiness score on the Cantril Ladder scale (0 = worst possible life, 10 = best possible life)         |
| gdp_per_capita          | Economic output per person — log scale, reflects contribution of income to happiness                   |
| social_support          | Perceived availability of someone to count on in times of trouble                                      |
| healthy_life_expectancy | Expected number of years lived in good health                                                          |
| freedom                 | Satisfaction with freedom to make key life choices                                                     |
| generosity              | Charitable giving behavior relative to GDP                                                             |
| corruption              | Perception of low corruption in government and business — higher value means less corruption perceived |


## Limitations:
- Missing Data:
     - The app currently handles missing data by dropping rows with NaN values (`dropna`). If a user uploads a dataset with heavy missing values, it may significantly reduce the sample size.
- Categorical Variables:
     - While the app encodes categorical text columns into numeric codes, distance-based algorithms (like K-Means) generally perform better with encoded variables or continuous data.
- Hierarchical Scalability:
     - Hierarchical clustering and its dendrogram visual can become difficult to read if a user uploads a very large dataset.

## Installation Instructions:
1. Clone this repository
2. Install dependencies and versions
    `pip install streamlit==1.32.0 pandas==2.2.1 numpy==1.26.4 matplotlib==3.8.3 scikit-learn==1.4.1 scipy==1.12.0`
3. Run the following command:
    `streamlit run MLUnsupervised.py`
4. Then open the local URL in your browser

## References and Further Reading:
World Happiness Report:
- [Official World Happiness Report (2026)](https://www.worldhappiness.report/ed/2026/)
- [Link to Kaggle Dataset](https://www.kaggle.com/datasets/hassanali789/world-happiness-report-2026-official-rankings)

Theory:
- [K-Means Clustering](https://www.geeksforgeeks.org/machine-learning/k-means-clustering-introduction/)
- [Hierarchical Clustering](https://www.geeksforgeeks.org/machine-learning/hierarchical-clustering/)
- [Principal Component Analysis](https://www.geeksforgeeks.org/data-analysis/principal-component-analysis-pca/)


Documentations:
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [SciPy Hierchical Clustering Documentation](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
