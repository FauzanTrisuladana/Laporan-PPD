print(df.duplicated().sum())
df.drop_duplicates(inplace=True)