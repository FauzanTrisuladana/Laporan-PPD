from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))

X = df[['bath', 'balcony', 'bhk', 'area_type']]
y = df['price']

X = pd.get_dummies(X, columns=['area_type'], drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Shape of X_train:", X_train_scaled.shape)
display(pd.DataFrame(X_train_scaled, columns=X.columns).head())
