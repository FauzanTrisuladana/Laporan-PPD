# imputasi missing value
df['bmi'].fillna(df['bmi'].mean(), inplace=True)
