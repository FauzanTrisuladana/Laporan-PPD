df['Age'] = df['Age'].fillna(df['Age'].median())
# df['Age'] = df['Age'].fillna(df['Age'].mean()) kalau mau mean

df['Cabin'] = df['Cabin'].fillna(df['Cabin'].value_counts().index[0])
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].value_counts().index[0])

display(df.isnull().sum())