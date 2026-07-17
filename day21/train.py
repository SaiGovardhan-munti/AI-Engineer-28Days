from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


sentence = [
    "I absolutely love this product, it exceeded my expectations.",
    "The service was excellent and the staff were very friendly.",
    "This is the worst experience I have ever had.",
    "I am very disappointed with the quality of the item.",
    "The movie was amazing and I would watch it again.",
    "The delivery was late and the package arrived damaged."
]

labels = [
    "positive",
    "positive",
    "negative",
    "negative",
    "positive",
    "negative"
]

vetorizer = TfidfVectorizer()
model = LogisticRegression(max_iter=200)
x = vetorizer.fit_transform(sentence)
model.fit(x, labels)
joblib.dump(vetorizer, "day21/vetorizer.pkl")
joblib.dump(model, "day21/model.pkl")