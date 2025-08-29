


# ☕ Coffee Sales Prediction

This project analyzes coffee sales data and builds a **machine learning regression model** to predict revenue (`money`) based on various factors such as time of day, weekday, and coffee type.

## 📌 Features

* Data preprocessing:

  * Dropping irrelevant columns
  * Extracting date & time features
  * One-hot encoding categorical variables
* Exploratory Data Analysis (EDA): summary statistics & insights
* Model building using **RandomForestRegressor**
* Performance evaluation using **R²** and **Mean Squared Error (MSE)**

## 📊 Results

* **Model Used:** RandomForestRegressor
* **Performance:**

  * Mean Squared Error (MSE): **0.31**
  * R² Score: **0.99**

This indicates the model fits the data very well and can accurately predict sales revenue.

## ⚙️ Requirements

Install dependencies using:

```bash
pip install pandas scikit-learn matplotlib seaborn numpy
```

## 🚀 How to Run

1. Clone this repository
2. Place the dataset `Coffe_sales.csv` in the working directory
3. Open the notebook and run all cells:

   ```bash
   jupyter notebook Coffee.ipynb
   ```
4. Review the analysis and model performance

