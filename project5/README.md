# 🌸 Iris Flower Classification using ANN (Keras + TensorFlow)

A simple **Artificial Neural Network (ANN)** model to classify **Iris flowers** into three species:
- Setosa 🌱
- Versicolor 🌿
- Virginica 🌸

This project demonstrates how to build, train, and evaluate a neural network using **Keras (TensorFlow backend)** on the classic **Iris dataset**.

---

## 📊 Dataset
- The dataset comes from **scikit-learn's built-in Iris dataset**.
- Features:
  - Sepal length
  - Sepal width
  - Petal length
  - Petal width
- Target: Flower species (3 classes)

---

## ⚙️ Tech Stack
- **Python 3**
- **TensorFlow / Keras**
- **Scikit-learn**
- **Matplotlib, Seaborn** (for visualization)

---

## 🧠 Model Architecture
- Input Layer: 4 features
- Hidden Layer 1: 10 neurons, ReLU activation
- Hidden Layer 2: 8 neurons, ReLU activation
- Output Layer: 3 neurons, Softmax activation

Loss function: `categorical_crossentropy`  
Optimizer: `adam`  
Metric: `accuracy`

---

## 📈 Results

- Achieved 95–98% accuracy on test data 🎯
- Confusion Matrix shows excellent classification
- Training curves demonstrate smooth convergence

---

## 👩🏻‍💻 Author

[Bhumika Yeole](www.linkedin.com/in/bhumikayeole)
