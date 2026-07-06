from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import argparse
from sklearn.tree import DecisionTreeClassifier


iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.25)

#create_model

model = LogisticRegression(max_iter=200)
model_dt = DecisionTreeClassifier()
model.fit(x_train,y_train)
model_dt.fit(x_train, y_train)
prediction_lr = model.predict(x_test)
prediction_dt = model_dt.predict(x_test)

#accuracy 
Accuracy_lr = accuracy_score(y_test, prediction_lr)
Accuracy_dt = accuracy_score(y_test, prediction_dt)

print(f"Accuracy_logisticRegression is : {Accuracy_lr}")
print(f"Accuracy_decissiontree is : {Accuracy_dt}")

best_model = model_dt if Accuracy_dt > Accuracy_lr else model
print(f"Best model for prediciton is: {best_model}")

parser = argparse.ArgumentParser()
parser.add_argument("--sepal-length", type= float)
parser.add_argument("--sepal-width", type=float)
parser.add_argument("--petal-length", type=float)
parser.add_argument("--petal-width", type=float)
args = parser.parse_args()

input_data = [[args.sepal_length, args.sepal_width, args.petal_length, args.petal_width]]
result = best_model.predict(input_data)
species = ["setosa", "versicolor", "virginica"]

print(f"result:{species[result[0]]}")