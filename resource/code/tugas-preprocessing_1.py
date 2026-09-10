df_X = df.drop(['Loan_ID', 'Loan_Status'], axis=1)
df_y = df[['Loan_Status']]

le = LabelEncoder()
df_y = le.fit_transform(df_y['Loan_Status'])

# yang null
# kalau numerik, pakai median
df_X['Loan_Amount_Term'] = df_X['Loan_Amount_Term'].fillna(df_X['Loan_Amount_Term'].median())
df_X['Credit_History'] = df_X['Credit_History'].fillna(df_X['Credit_History'].median())

# kalau kategorikal, pakai mode (nilai tersering)
df_X['Gender'] = df_X['Gender'].fillna(df_X['Gender'].mode()[0])
df_X['Dependents'] = df_X['Dependents'].fillna(df_X['Dependents'].mode()[0])
df_X['Self_Employed'] = df_X['Self_Employed'].fillna(df_X['Self_Employed'].mode()[0])

cats = df_X.select_dtypes(include=['object', 'bool']).columns
cat_features = list(cats.values)
le = LabelEncoder()
for i in cat_features:
    df_X[i] = le.fit_transform(df_X[i].astype(str))

# Menyimpan X dan y menjadi numpy arrays
X = df_X.astype(float).values
y = df_y.astype(float)

# Split data: train 70% test 30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scaling
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
