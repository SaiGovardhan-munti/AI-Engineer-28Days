from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


iris = load_iris()
x = iris.data
y = iris.target


x_train , x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

#create model

model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)
prediction = model.predict(x_test)

#accuracy 

Accuracy = accuracy_score(y_test,prediction)
print(f"Accuracy is : {Accuracy}")

for i in range(5):
    print(f"Predicted: {prediction[i]} | Actual: {y_test[i]}")



