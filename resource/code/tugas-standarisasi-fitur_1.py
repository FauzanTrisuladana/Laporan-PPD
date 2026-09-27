X_task = df_task.astype(float).values
scaler_task = StandardScaler()
X_task_scaled = scaler_task.fit_transform(X_task)
print(X_task_scaled.shape)
