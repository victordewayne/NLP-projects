from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

texts = [
    "Win a free iphone now!",
    "Your account has been suspended",
    "Let's meet for lunch tomorrow",
    "Congratulations, you won a prize!",
    "Can you send the report today?",
    "Free tickets to bahamas, click now!",
    "Reminder: doctor appointment at 4PM"
]

labels = [1, 1, 0, 1, 0, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy: ", accuracy_score(y_test, y_pred))