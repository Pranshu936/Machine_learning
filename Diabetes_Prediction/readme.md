

# Diabetes Prediction using K-Nearest Neighbors (KNN)

This project applies the **K-Nearest Neighbors (KNN)** algorithm to predict whether a patient has diabetes based on diagnostic measurements. The model is trained and tested using a publicly available diabetes dataset.

## Dataset

The dataset contains medical predictor variables such as:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

The target variable is:

* **Outcome**: `1` (diabetic) or `0` (non-diabetic)

## Project Workflow

1. **Data Loading**
   Import dataset and examine basic statistics.

2. **Data Preprocessing**

   * Handle missing or zero values where applicable.
   * Feature scaling to normalize the data.

3. **Model Training**

   * Use **K-Nearest Neighbors** classifier.
   * Tune the value of `k` for best accuracy.

4. **Evaluation**

   * Accuracy score
   * Confusion matrix
   * Classification report

## Requirements

Install dependencies before running the notebook:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Usage

1. Open the notebook:

   ```bash
   jupyter notebook "Diabetes dataset-KNN.ipynb"
   ```
2. Run the cells step-by-step to:

   * Load and preprocess data
   * Train the KNN model
   * Evaluate performance

## Output

The notebook displays:

* Accuracy of the KNN model
* Confusion matrix visualization
* Best `k` value for prediction

