# cek kategorikal atribut
df_X = df.drop(columns=['CLIENTNUM', 'Attrition_Flag'], axis=1)
df_y = df['Attrition_Flag']
cats = df_X.select_dtypes(include=['object', 'bool']).columns
print(cats)
