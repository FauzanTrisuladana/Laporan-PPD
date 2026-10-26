X_train, X_test, y_train, y_test = train_test_split(
    df_X, df_y, test_size=0.3, random_state=8
)

# scaling
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
