# 💳 Credit Card Fraud Detection App

A Streamlit-powered web app designed to identify fraudulent credit card transactions using a Logistic Regression model. Instantly predict fraud by uploading transaction data in bulk or entering individual transaction details.

---

## 🚀 Highlights

- ✅ *Batch predictions* through CSV file uploads
- ✍ *Single transaction analysis* via manual data entry
- 📊 *Comprehensive prediction summaries* with visual insights
- 🧁 *Dynamic pie charts* showing fraud vs. normal transactions
- 💰 *Transaction amount breakdown* by type
- 📥 *Exportable prediction results* for further analysis

---

## 📁 Data Source

This application leverages the [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), featuring:

- *284,807 transactions* collected over two days in September 2013
- PCA-transformed features V1 to V28
- Columns: Time, Amount, and Class
- Class = 1 → Fraudulent | Class = 0 → Normal

---

## 🛠 Tech Stack

- [Python 3.12+](https://www.python.org)
- [Streamlit](https://streamlit.io/)
- [Scikit-learn](https://scikit-learn.org)
- [Pandas & NumPy](https://pandas.pydata.org)
- [Plotly](https://plotly.com/python/)