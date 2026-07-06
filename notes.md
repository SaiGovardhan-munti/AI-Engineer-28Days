class — blueprint for creating objects
__init__ — runs when object is created
self — refers to the current object
__str__ — controls what print() shows
inheritance — class Child(Parent)
super().__init__() — calls parent's __init__


polymorphism — same method name, different behavior in each class
abstraction — hide complexity, show only interface (ABC, @abstractmethod)


# ML Fundamentals + scikit-learn
supervised — labeled data, predict output
unsupervised — no labels, find patterns
classification — predict category, regression — predict number
overfitting — high train, low test (big gap)
underfitting — both low
train_test_split(X, y, test_size=0.2) — 80/20 split
model.fit(X_train, y_train) — train
model.predict(X_test) — predict
accuracy_score(y_test, predictions) — measure accuracy
precision — how many predicted yes were actually yes
recall — how many actual yes did we catch