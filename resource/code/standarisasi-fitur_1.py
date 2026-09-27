X=df_new.astype(float).values
scaller=StandardScaler().fit(X)
X_new=scaller.transform(X)
X_new
print(X_new.shape)
