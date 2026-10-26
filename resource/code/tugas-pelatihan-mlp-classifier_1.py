# mulai learning
model = MLPClassifier(max_iter=500)

# model=MLPClassifier(max_iter=1000, random_state=42, activation='logistic')
model.fit(X_train, y_train)
