# 🎓 Student Performance Clustering

This project applies **Unsupervised Machine Learning** to group students based on their academic performance (grades, quizzes, projects, participation, etc.).  
We use **PCA** for dimensionality reduction, **KMeans** for clustering, and **Silhouette Analysis** to evaluate the quality of clusters.  

---

## 🎯 Objectives
- Identify **student performance groups** (e.g., High Performers, Average Students, Needs Support).  
- Explore **patterns in academic data** using unsupervised learning.  
- Apply **PCA** to reduce dimensions for visualization and highlight underlying trends.  
- Use **KMeans clustering** to segment students into meaningful categories.  
- Evaluate cluster quality with **Silhouette Score**.  
- Provide **interactive visualizations** with Plotly for better insights.  

---

## 📌 Project Overview
- 📊 **Goal**: Identify meaningful groups of students such as *High Performers*, *Average Students*, and *Students Needing Support*.  
- 🛠 **Tech Stack**: `Python`, `pandas`, `scikit-learn`, `plotly`, `matplotlib`, `seaborn`  
- 🔍 **Approach**:
  1. Load & clean dataset (handle missing values, impute if needed).
  2. Standardize features for fair comparison.
  3. Apply **PCA** to reduce dimensions for visualization.
  4. Cluster students using **KMeans**.
  5. Evaluate clusters with **Silhouette Score**.
  6. Visualize results using **Plotly** interactive scatter plots.

---

## 📂 Dataset
We use the [**Student Performance & Behavior Dataset**](https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset) from Kaggle.  

**Features:**
- `Quizzes_Avg` → Average quiz scores  
- `Projects_Score` → Project evaluations  
- `Participation_Score` → Classroom participation  
- `Total_Score` → Combined performance score  

---

## 👩🏻‍💻 Author
[Bhumika Yeole](www.linkedin.com/in/bhumikayeole)
