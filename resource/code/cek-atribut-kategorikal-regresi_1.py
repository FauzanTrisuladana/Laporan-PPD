# cek kategori attribut
df_X = df.drop(['id', 'date', 'price'], axis=1)
df_y = df[['price']]
cats = df_X.select_dtypes(include=['object', 'bool']).columns
print(cats)
