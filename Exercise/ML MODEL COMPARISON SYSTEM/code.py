from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

X = iris.data
y = iris.target

X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LogisticRegression(max_iter=200)
rf_model = RandomForestClassifier(random_state=42)

class MLModelService :
    def __init__(self, model):
        self.model = model 
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    def predict(self, X_test):
        return self.model.predict(X_test)
    def evaluate(self, X_test, y_test):
        prediction = self.predict(X_test)
        return accuracy_score(y_test, prediction) 

service = MLModelService(lr_model)
service.train(X_train, y_train)
prediction = service.predict(X_test)
evaluate = service.evaluate(X_test, y_test)

rf_service = MLModelService(rf_model)
rf_service.train(X_train, y_train)
rf_predict = rf_service.predict(X_test)
rf_acc = rf_service.evaluate(X_test, y_test)
print("Random Forest Trained Succesfully ")
print(f"Features Shape : {X.shape}")
print(f"Target Shape : {y.shape}")
print(f"Feature Name : {iris.feature_names}")
print(f"Target Names : {iris.target_names}")
print(f"First Sample : {X[0]}")
print(f"First Label : {y[0]}")
print(f"X_train Shape : {X_train.shape}")
print(f"X_test Shape : {X_test.shape}")
print(f"y_train Shape : {y_train.shape}")
print(f"y_test Shape : {y_test.shape}")
print(f"ML Model Service : {service.model}")

print("Model Comparision ")
print(f"Logistic Regression Accuracy  : {evaluate }%")
print(f"Random Forest Accuracy : {rf_acc  }%")

if evaluate > rf_acc :
    print("Better Model : Logistic Regression")
elif evaluate < rf_acc :
    print("Better Model : Random Forest ")
else:
    print("Result : Both model have equal Accuaracy (Tie)")