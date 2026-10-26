# cek kategori attribut
df_X = df.drop(['Blood Glucose Level(BGL)'], axis=1)
df_y = df['Blood Glucose Level(BGL)']

# transform 'Diabetic/NonDiabetic (D/N)' D=1 dan N=0
df_X['Diabetic/NonDiabetic (D/N)'] = df_X['Diabetic/NonDiabetic (D/N)'].map(
    {'D': 1, 'N': 0}
)

cats = df_X.select_dtypes(include=['object', 'bool']).columns
print(cats)
