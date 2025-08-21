
# 🚖 Ride Booking Analysis & Prediction

## 📌 Project Overview

This project analyzes ride booking data (\~150k records, 21 features) to solve two key business problems:

1. **Booking Status Prediction** → Predict whether a ride will be *Completed, Cancelled, Incomplete, or No Driver Found*.
2. **Customer Churn Modeling** → Identify customers at risk of leaving the platform.

The goal is to reduce cancellations, improve completion rates, and design targeted retention strategies.

---

## 📊 Data Summary

* **Size:** 150,000 rows × 21 columns
* **Data Types:** mix of numerical & categorical (ratings, ride values, locations, vehicle type, payment method).
* **Missing Values:** in Avg VTAT, Avg CTAT, Booking Value, Ride Distance, and Ratings.
* **Target (for booking model):** `Booking Status`
* **Target (for churn model):** derived using ride history (low completion rate + low ride frequency).

---

## 🔎 Key Findings

* Most bookings are **Completed**, but *Cancelled by Driver/Customer* and *No Driver Found* are significant.
* New time features (`Hour_of_Day`, `Day_of_Week`) improved model explainability.
* Customer aggregates: `total_rides`, `completion_rate`, `avg_booking_value`, `avg_ride_distance`.
* **SMOTE** was applied to address class imbalance in booking status.

---

## 🤖 Modeling

### 1. Booking Status Prediction

* **Models Tested:** Logistic Regression, Random Forest, Gradient Boosting.
* **Best Models:** Random Forest & Gradient Boosting (outperformed Logistic Regression).
* **Important Features:** `Avg VTAT`, `Ride Distance`, `completion_rate`, `Avg CTAT`.
* **Use Case:** Early cancellation prediction → reassign drivers & reduce failed rides.

### 2. Customer Churn Modeling

* **Churn Definition:** `completion_rate < 0.5` **AND** `total_rides ≤ 2`. (\~38% churn rate).
* **Models Tested:** Logistic Regression, Random Forest, Gradient Boosting.
* **Results:** Achieved perfect metrics (Precision, Recall, F1, ROC-AUC = 1.0).
* **Key Drivers of Churn:** `completion_rate`, `avg_booking_value`, `avg_ride_distance`.
* **Use Case:** Identify churn-prone customers for promotions, loyalty offers, re-engagement campaigns.

---

## 📈 Business Impact

* **Operational:** Reduce failed bookings by predicting cancellations.
* **Customer Retention:** Proactively target at-risk customers with discounts or incentives.
* **Revenue:** Improved completion rates and reduced churn directly increase revenue.

---

## 🛠️ Tech Stack

* **Python** (pandas, scikit-learn, imbalanced-learn)
* **Models:** Logistic Regression, Random Forest, Gradient Boosting
* **Tools:** Jupyter, matplotlib, joblib (for model persistence)

---



## 📂 Project Artifacts

* `booking_status_pipeline.joblib` → Booking prediction model
* `churn_pipeline.joblib` → Churn prediction model
* `booking_status_metrics.json`, `churn_metrics.json` → Evaluation reports

---


Would you like me to make this README more **resume-style (1-page, professional bullet points)** or **GitHub-style (detailed with sections like above)**?
