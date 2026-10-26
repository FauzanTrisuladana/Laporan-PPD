df_X = df.drop(['id', 'date', 'price'], axis=1)
df_y = df['price']

imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(df_X)
y = df_y.astype(float).values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

reg = MLPRegressor()
reg.fit(X_train, y_train)

print('coef of determination training ', reg.score(X_train, y_train))
print('coef of determination testing ', reg.score(X_test, y_test))

print('prediction')
y_pred = reg.predict(X_test)
print(y_pred[:10])
print('real value')
print(y_test[0:10])
