# 🛫 Airline Tweet Sentiment Analyzer

This web app, built with Streamlit, evaluates the sentiment of tweets aimed at airlines. It leverages a Naive Bayes classifier trained on the *Tweets.csv* dataset to determine if a tweet is **Positive**, **Neutral**, or **Negative**.

## 🌟 Key Highlights

- 🧭 Instantly analyze the sentiment of airline tweets (positive, neutral, negative)
- 📈 Visualize model accuracy and performance metrics
- 🧽 Automated text cleaning, lemmatization, and stopword filtering
- 🧩 Naive Bayes algorithm trained on authentic Twitter data
- 💻 Simple and interactive Streamlit user interface

---

## 🗂️ Data Source

The model is trained on the [Tweets.csv](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) dataset from Kaggle:
- Contains 14,640 tweets about major U.S. airlines
- Each tweet labeled as positive, neutral, or negative
- Only includes tweets with sentiment confidence ≥ 0.5