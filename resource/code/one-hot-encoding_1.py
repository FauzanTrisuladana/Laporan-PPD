# ohe = OneHotEncoder(sparse_output=False, drop='first')
ohe = OneHotEncoder(sparse_output=False)

ohe.fit(df_X[['Sex', 'Embarked']])

df_ohe = ohe.transform(df_X[['Sex', 'Embarked']])

df_ohe