df_X = df.drop(['date', 'Occupancy'], axis=1)
df_y = df['Occupancy']

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.3, random_state=8)

scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

print(f"Dimensi X_train: {X_train.shape}, X_test: {X_test.shape}")
print(f"Distribusi y_train:\n{y_train.value_counts()}")
