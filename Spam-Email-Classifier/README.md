# Spam Email Classifier

## 📌 Overview
This project focuses on building a **Spam Email Classifier** using **synthetic data generation** and **machine learning**.  
The workflow spans from dataset creation to deployment, enabling an interactive spam detection system.

---

## 📺 Watch it live here
[Live Demo](https://bhumikayeole-spam-email-classifier.hf.space/?__theme=system&deep_link=SJlQujmPIZs)

---

## 🔑 Objectives
- Generate a labeled dataset of **spam** and **ham** emails using **GPT-2**.
- Perform **Exploratory Data Analysis (EDA)** to understand email patterns.
- Train a **Naive Bayes classifier** with **TF-IDF vectorization**.
- Deploy the model via **Gradio** and **Hugging Face Spaces** for real-time usage.

---

## 📂 Project Structure
```bash
Spam-Email-Classifier/
├── Final_Report.docx
├── Spam_Classifier_Slides.pptx.url
├── Notebooks/
│   ├── 1_EDA.ipynb
│   ├── 2_GPT2_Email_Generation.ipynb
│   ├── 3_ML_Model_Training.ipynb
│   └── 4_Visualization.ipynb
├── Data/
│   ├── synthetic_email_dataset.csv
├── Models/
│   ├── spam_classifier_nb.pkl
│   └── tfidf_vectorizer.pkl
├── clean_notebooks.py
└── README.md
```
---

## 📊 Dataset
- **Source**: Generated synthetically using GPT-2 with custom prompts.
- **Classes**:
  - `0` → Ham (legitimate emails)
  - `1` → Spam (promotional/scam emails)
- Balanced dataset to avoid bias during training.

---

## 🔍 Exploratory Data Analysis (EDA)
- Distribution of spam vs ham emails.
- Frequent spam words: *free, win, offer, click, limited*.
- Frequent ham words: *meeting, project, schedule, update*.
- EDA insights informed preprocessing and model design.

---

## 🤖 Model Training
- **Preprocessing**: TF-IDF Vectorization
- **Algorithm**: Multinomial Naive Bayes
- **Metrics**:
  - Accuracy: >90%
  - Balanced Precision and Recall
  - Strong F1-score

---

## 🚀 Deployment
- Frontend built using **Gradio**.
- Hosted on **Hugging Face Spaces** for free public access.
- Users can input any email text and get a **Spam/Ham prediction** instantly.

---

## 📌 Conclusion
- Successfully built a spam email classifier from scratch.
- Demonstrated full ML pipeline: **Data Generation → EDA → Model Training → Deployment**.
- **Future Work**:
  - Test on real-world email datasets.
  - Experiment with advanced transformer-based classifiers (BERT, RoBERTa).
  - Improve interpretability with explainable AI tools.

---

