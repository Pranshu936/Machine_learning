
# Resume–Job Matching using Machine Learning

This project applies **Natural Language Processing (NLP)** and **Machine Learning** techniques to predict the similarity between **resumes** and **job descriptions**. The goal is to automate the process of evaluating candidate-job matches.

## 📌 Features

* Data preprocessing and cleaning
* Text representation using **TF-IDF** and **Sentence-BERT embeddings**
* Model building for:

  * **Classification** (High Match vs Low Match)
  * **Regression** (Match Score prediction)
* Model evaluation with metrics:

  * Accuracy, Precision, Recall, F1-Score (Classification)
  * MAE, RMSE (Regression)
* Comparison between linear models and ensemble methods

## 📊 Results

* **Classification:** Logistic Regression (TF-IDF) achieved the best performance with **81% accuracy**.
* **Regression:** Ridge Regression (TF-IDF) had the lowest error with **MAE = 0.5670, RMSE = 0.7305**.
* **Conclusion:** Simpler models with TF-IDF embeddings outperformed more complex Sentence-BERT + Tree-based models.

## ⚙️ Requirements

Install dependencies using:

```bash
pip install pandas scikit-learn matplotlib seaborn numpy
pip install sentence-transformers
```

## 🚀 How to Run

1. Clone this repository
2. Place the dataset `resume_job_matching_dataset.csv` in the working directory
3. Open the notebook and run all cells:

   ```bash
   jupyter notebook Untitled4.ipynb
   ```
4. Review the output and evaluation metrics





