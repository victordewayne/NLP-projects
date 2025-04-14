import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 

with open("intent.json") as f:
    data = json.load(f)

x, y = [], []
for intent in data['intents']:
    for pattern in intent['patterns']:
        x.append(pattern)
        y.append(intent['tag'])

vectorizer = TfidfVectorizer()
X_vectors = vectorizer.fit_transform(x)

clf = LogisticRegression()
clf.fit(X_vectors, y)

def chat():
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        user_vec = vectorizer.transform([user_input])
        prediction = clf.predict(user_vec)[0]


        for intent in data["intents"]:
            if intent ["tag"] == prediction:
                response = random.choice(intent["responses"])
                print("Chatbot: ", response)

chat()