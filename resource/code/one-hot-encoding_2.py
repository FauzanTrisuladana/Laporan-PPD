cats = df_X.select_dtypes(include=['object', 'bool']).columns
cat_features = list(cats.values)
cat_en = LabelEncoder()

for i in cat_features:
    df_X[i] = cat_en.fit_transform(df_X[i])

df_X