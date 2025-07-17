# Iris Classifier using TensorFlow (1-Nearest Neighbor)

This project implements a simple 1-Nearest Neighbor classifier using TensorFlow on the Iris dataset.  
It uses L1 distance to classify iris flowers into one of three species: Setosa, Versicolor, or Virginica.

## 📂 Files
- `iris.txt`: Dataset containing 150 rows, each with 4 features and a label.
- `main.py`: Python script that loads the dataset, processes it, and performs classification.

## 🧪 Features
Each sample includes:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## 🧠 Model
- Classifier: 1-Nearest Neighbor (with L1 distance)
- Framework: TensorFlow (v1 style placeholders and sessions)

## ⚙️ How it works
1. Reads and balances the dataset.
2. Splits into training and testing sets (70% train, 30% test).
3. Computes the L1 distance between test and train samples.
4. Predicts the class of the closest training sample.
5. Outputs prediction and calculates accuracy.
