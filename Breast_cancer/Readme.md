
# Breast Cancer Data Analysis & Classification Models

This repository contains a Jupyter Notebook that loads, preprocesses, and models breast cancer data using multiple machine learning algorithms: **Logistic Regression**, **Support Vector Machine (SVM)**, and **Random Forest**.

---

## Notebook Overview
The notebook (`Bcancer.ipynb`) follows these steps:

### 1. Importing Libraries
- **pandas** for data handling
- **numpy** for numerical operations
- **matplotlib / seaborn** for visualization
- **scikit-learn** for preprocessing, modeling, and evaluation

### 2. Loading the Dataset
- Reads the dataset from:
  ```python
  df = pd.read_csv('/content/Breast_cancer_dataset.csv')


* Displays the first rows and dataset info.

### 3. Data Exploration

* Checks dataset dimensions and column details.
* Finds that `Unnamed: 32` contains only null values and removes it.
* Examines the `diagnosis` column (B = Benign, M = Malignant).

### 4. Data Preprocessing

* Converts `diagnosis` from categorical to numeric (`0` and `1`).
* Scales numerical features using `StandardScaler`.

### 5. Train-Test Split

* Splits the dataset into:

  * **Features (X)**
  * **Target (y)**
* Uses 80% training, 20% testing:

  ```python
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```

### 6. Model Training

* Trains three models:

  * Logistic Regression
  * Support Vector Machine (SVM)
  * Random Forest Classifier

### 7. Model Evaluation

* Evaluates each model using:

  * Accuracy
  * Precision
  * Recall
  * F1-score
* **Performance:**

  * Logistic Regression: Accuracy 0.9737
  * SVM: Accuracy 0.9737
  * Random Forest: Accuracy 0.9649

### 8. Conclusion

* Logistic Regression and SVM slightly outperformed Random Forest in accuracy and F1-score.
* All models performed very well, showing strong predictive ability.

---

## Requirements

Install the following dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

---

## Running the Notebook

1. Clone this repository or download the files.
2. Install the dependencies above.
3. Open the notebook:

```bash
jupyter notebook Bcancer.ipynb
```

4. Run all cells to reproduce the analysis and model results.

---

