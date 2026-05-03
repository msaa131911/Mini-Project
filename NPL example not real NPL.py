#NPL example not real NPL
import pandas as pd

df = pd.read_csv("E:\ALL_IN_ONE\DATA\AI_Student_Life_Pakistan_2026.csv")
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


texts = [
    "average age koto",
    "age mean bolo",
    "gender count koto",
    "show data",
]

labels = [
    "mean",
    "mean",
    "count",
    "show"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def detect_column(cmd, df):
    for col in df.columns:
        if col.lower() in cmd.lower():
            return col
    return None
def ai_query(cmd):
    X_input = vectorizer.transform([cmd])
    action = model.predict(X_input)[0]

    col = detect_column(cmd, df)

    if action == "mean" and col:
        return df[col].mean()

    elif action == "count" and col:
        return df[col].value_counts()

    elif action == "show":
        return df.head()

    else:
        return "bujhte pari nai "
    
while True:
    user_query = input("User Query: ")
    print(ai_query(user_query))

    if user_query.lower() == "q":
        break
