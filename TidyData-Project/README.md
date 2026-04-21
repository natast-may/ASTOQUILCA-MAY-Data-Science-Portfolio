# Tidy Data Project: 2008 Olympic Medalists

## Project Overview:
This project focuses on cleaning and transforming a messy, wide-format dataset using **tidy data principles**. 

📍 **GOAL 1** - apply tidy data principles so that: 
- each variable has its own column
- each observation has its own row
- each cell contains only one value

📍 **GOAL 2** - generate visualizations and summary statistics
- my focus is medal distributions by gender and sport

## Dataset Description
Dataset adapted from source: [2008 Olympic Medalists](https://edjnet.github.io/OlympicsGoNUTS/2008/)

📍 Notes:
- The original dataset contained 71 columns
- Multiple variables stored in one column (`Gender` + `Sport` combined in headers), making analysis difficult
- Wide format results in many unnecessary `NaN` values

📍 Data was pre-processed by:
- melting 71 columns into long format with `pd.melt`
- splitting the combined `Gender_Sport` column into two distinct variables using `str.split()`
- filtering out `NaN` values with `.dropna()`
  
---

## Visualization examples:
**🎖️ Example 1**
<img width="600" height="400" alt="Screenshot 2026-03-20 at 7 02 24 PM" src="https://github.com/user-attachments/assets/98f126f7-8457-4cd4-8e88-1322109a2b01" />

- "Athletics" is the sport with the most female medalists (~80 medalists).
-  The top 5 sports with the most female medalists are athletics, swiming, rowing, association football, and field hockey

**🎖️ Example 2**
<img width="600" height="550" alt="Screenshot 2026-03-20 at 7 02 55 PM" src="https://github.com/user-attachments/assets/caf7d8c1-91ff-4921-b739-9a96cc002605" />

- Overall, there were 199 more male medalists than female medalists at the 2008 Olympics
---

## Installation Instructions:
1. **Clone the repository** and place `olympics_08_medalists.csv` in the project directory.

2. **Install dependencies:**
```bash
   pip install pandas seaborn matplotlib
```

3. **Open and run the notebook:**
```bash
   jupyter notebook Tidy_Data_Notebook.ipynb
```
   Execute cells in order.

---

## References and Further Reading:
- Pandas cheat sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- Tidy Data Principles (Wickham): https://vita.had.co.nz/papers/tidy-data.pdf


  
