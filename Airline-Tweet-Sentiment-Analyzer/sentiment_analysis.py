import pandas as pd
import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

nltk.download('stopwords')
nltk.download('wordnet')

data = pd.read_csv('/content/sentiment_analysis.csv')
data = data[data['airline_sentiment_confidence'] >= 0.5]

X = data['text']
Y = data['airline_sentiment']

stop_words = stopwords.words('english')
punctuations = string.punctuation
lemmatizer = WordNetLemmatizer()

clean_data = []
for text in X:
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [lemmatizer.lemmatize(word) for word in text if word not in stop_words and word not in punctuations]
    clean_data.append(' '.join(text))

sentiments = ['negative', 'neutral', 'positive']
Y = Y.apply(lambda x: sentiments.index(x))

vectorizer = CountVectorizer(max_features=5000, stop_words=['virginamerica', 'united'])
X_vect = vectorizer.fit_transform(clean_data).toarray()

X_train, X_test, Y_train, Y_test = train_test_split(X_vect, Y, test_size=0.3)
model = MultinomialNB()
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)

print(classification_report(Y_test, y_pred))

