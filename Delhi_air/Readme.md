
# Delhi Air Quality Analysis & Anomaly Detection

This repository contains a Jupyter Notebook that analyzes Delhi's air quality data, detects anomalies using **Isolation Forest**, and builds a **Logistic Regression** model to predict anomaly status.

---

## Notebook Overview
The notebook (`delhiair.ipynb`) follows these steps:

### 1. Importing Libraries
- **pandas** for data handling
- **numpy** for numerical operations
- **matplotlib / seaborn** for visualization
- **scikit-learn** for modeling and evaluation

### 2. Loading the Dataset
- Reads the dataset from:
  ```python
  df = pd.read_csv('/content/final_dataset.csv')


* Displays the first few rows, data info, descriptive statistics, and unique values.

### 3. Data Exploration

* Dataset contains **1461 rows and 12 columns**.
* Features include PM2.5, PM10, NO2, SO2, CO, Ozone, AQI, and other pollutant measures.
* No missing values detected.
* AQI shows a wide range, indicating varying air quality levels.

### 4. Anomaly Detection with Isolation Forest

* Trains an **Isolation Forest** model to detect extreme pollution events.
* Anomalies are primarily characterized by:

  * Higher concentrations of pollutants
  * Significantly higher AQI values (mean AQI for anomalies: **323.56** vs overall mean: **202.21**)
* Adds a binary feature `is_anomaly_binary` to the dataset.

### 5. Train-Test Split

* Features (`X`) = Air quality metrics
* Target (`y`) = `is_anomaly_binary`
* Splits data into **80% training** and **20% testing**.

### 6. Logistic Regression Model

* Trains a Logistic Regression classifier on the training set.
* Predicts anomaly status based on air quality indicators.

### 7. Model Evaluation

* Accuracy: **0.9488**
* Precision: **0.8718**
* Recall: **0.7727**
* F1-score: **0.8193**

### 8. Conclusion

* Isolation Forest successfully identified high-pollution anomalies.
* Logistic Regression achieved strong predictive performance for anomaly detection.

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
jupyter notebook delhiair.ipynb
```

4. Run all cells to reproduce the analysis and results.

---


