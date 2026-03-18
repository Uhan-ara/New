import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import preprocess

df = pd.read_csv("data/videos.csv")

df['clean_text'] = (df['title'] + " " + df['description']).apply(preprocess)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['clean_text'])

y = df['category']

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Train classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = MultinomialNB()
clf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))