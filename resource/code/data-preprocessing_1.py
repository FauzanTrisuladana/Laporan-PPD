df_X = df.drop(['id', 'date','price'], axis=1)
df_y = df['price']
cats = df_X.select_dtypes(include=['object', 'bool']).columns
print(cats)

df_X = df.drop(['id', 'date', 'price'], axis=1)
df_y = df['price']

# Ntah kenapa ada yang null
df_X['sqft_above'] = df_X['sqft_above'].fillna(df_X['sqft_above'].mean())

X = df_X.astype(float).values
y = df_y.astype(float).values