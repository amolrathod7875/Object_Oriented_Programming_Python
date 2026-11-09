# ML Model Comparison System

## Overview

This exercise demonstrates **composition** and a **shared interface** in Python by wrapping different scikit-learn estimators behind a single `MLModelService`. The service accepts any compatible model in its constructor and exposes `train`, `predict`, and `evaluate`, so the same workflow can run `LogisticRegression` and `RandomForestClassifier` on the Iris dataset without changing the service. Model performance is compared using `accuracy_score`, with an explicit tie case.

## Tasks

- [x] Load the Iris dataset from `sklearn.datasets`.
- [x] Split into training and testing sets (`random_state=42`).
- [x] Create an `MLModelService` that accepts a model in its constructor.
- [x] Implement `train(X_train, y_train)`.
- [x] Implement `predict(X_test)`.
- [x] Implement `evaluate(X_test, y_test)` using `accuracy_score`.
- [x] Use the service with `LogisticRegression` and `RandomForestClassifier`.
- [x] Print both test accuracies and identify the better-performing model.
- [x] If scores are tied, explicitly report a tie.

## Pass Checks

- [x] Both models train successfully using one shared service design.
- [x] Predictions are returned for the test set.
- [x] Accuracy scores are compared correctly and the better model (or a tie) is reported.
- [x] Composition is useful here: `MLModelService` depends on an injected estimator rather than hard-coding a specific model, so the same interface works for any sklearn-compatible model.

## Code

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LogisticRegression(max_iter=200)
rf_model = RandomForestClassifier(random_state=42)

class MLModelService:
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
print(f"Logistic Regression Accuracy  : {evaluate * 100}%")
print(f"Random Forest Accuracy : {rf_acc * 100 }%")

if evaluate > rf_acc:
    print("Better Model : Logistic Regression")
elif evaluate < rf_acc:
    print("Better Model : Random Forest ")
else:
    print("Result : Both model have equal Accuaracy (Tie)")
```

## How the Code Satisfies the Tasks

- **Dataset & split**: Loads Iris and performs an 80/20 train-test split with `random_state=42` for reproducibility.
- **Composition**: `MLModelService` stores the injected `model` and delegates to it (`fit`/`predict`), so the service is model-agnostic.
- **Shared interface**: Both `LogisticRegression` and `RandomForestClassifier` are trained, predicted, and evaluated through the same `MLModelService` API.
- **Evaluation & comparison**: `evaluate` returns `accuracy_score` (0–1). Accuracies are compared to select the better model, and an explicit tie branch reports equal accuracy.

## Running the example

Requires scikit-learn in the active Python environment:

```bash
pip install scikit-learn
cd "Exercise/ML MODEL COMPARISON SYSTEM"
python code.py
```

The script prints dataset/model details, both accuracies, and the comparison result. Output values may vary slightly by environment, but the comparison logic remains correct.
