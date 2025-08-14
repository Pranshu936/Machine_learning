
# Airline Flight Data Analysis & LightGBM Modeling

This repository contains a Jupyter Notebook that loads, explores, and models airline flight data using **LightGBM** — a high-performance gradient boosting framework.

---

## Notebook Overview
The notebook (`airline.ipynb`) follows these steps:

### 1. Importing Libraries
- **pandas** for data manipulation
- **numpy** for numerical operations
- **matplotlib / seaborn** for data visualization
- **lightgbm** for modeling
- **scikit-learn** for train-test splitting and evaluation metrics

### 2. Loading the Dataset
- Reads the dataset from:
  ```python
  df = pd.read_csv('/content/airlines_flights_data.csv')




### 3. Data Exploration

* Checks for missing values and data types.
* Looks at distributions of features.
* Identifies categorical and numerical variables.

### 4. Data Preprocessing

* Encodes categorical features as numeric.
* Handles missing values if present.
* Splits the dataset into:

  * **Features (X)**
  * **Target (y)**

### 5. Train-Test Split

* Uses `train_test_split` to create training and testing sets:

  ```python
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```

### 6. LightGBM Model Training

* Initializes and trains a LightGBM classifier:

  ```python
  import lightgbm as lgb
  model = lgb.LGBMClassifier()
  model.fit(X_train, y_train)
  ```

### 7. Model Evaluation

* Predicts on the test set.
* Calculates and prints performance metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score
* May include a confusion matrix for detailed evaluation.

### 8. Conclusion

* Summarizes model performance.
* Notes why LightGBM was chosen for efficiency and speed.

---

## Requirements

Install the following dependencies:

```bash
pip install pandas numpy matplotlib seaborn lightgbm scikit-learn jupyter
```

---

## Running the Notebook

1. Clone this repository or download the files.
2. Install the dependencies above.
3. Open the notebook:

```bash
jupyter notebook airline.ipynb
```

4. Run all cells to reproduce the analysis and model results.

---


