le = LabelEncoder()
le.fit(df_y)
df_y = le.fit_transform(df_y)
df_y