print("Missing Values:
", df.isnull().sum())

print(f"
Duplicate rows: {df.duplicated().sum()}")

df = df.drop_duplicates()
df['size'] = df['size'].fillna(df['size'].mode()[0])
df['bath'] = df['bath'].fillna(df['bath'].median())
df['balcony'] = df['balcony'].fillna(df['balcony'].median())
df.dropna(subset=['location'], inplace=True)
print("
Cleaned Missing Values:", df.isnull().sum().sum())
