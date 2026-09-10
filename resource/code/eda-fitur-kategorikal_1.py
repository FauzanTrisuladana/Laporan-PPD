df_X = df.drop(['id', 'stroke'], axis=1)
df_y = df[['stroke']]

cats = df_X.select_dtypes(include=['object', 'bool']).columns
print(cats)
