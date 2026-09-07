df_X = df.drop(['PassengerId', 'Name', 'Survived', 'Cabin', 'Ticket'], axis=1)
df_y = df['Survived']

cats = df_X.select_dtypes(include=['object', 'bool']).columns
print(cats)