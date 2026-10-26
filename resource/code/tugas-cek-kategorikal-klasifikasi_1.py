df_X = df.drop(['date', 'Occupancy'], axis=1)
df_y = df['Occupancy']

cats = df_X.select_dtypes(include=['object', 'bool']).columns
print(cats)
