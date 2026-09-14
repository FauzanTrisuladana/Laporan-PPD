df_X = df.drop(['car_ID', 'CarName', 'carbody', 'price'], axis=1)
df_y = df['price']

# Perform one-hot encoding for remaining categorical columns
df_X = pd.get_dummies(df_X, columns=['drivewheel', 'enginelocation', 'aspiration', 'fueltype', 'doornumber', 'enginetype', 'cylindernumber', 'fuelsystem'], drop_first=True)

X = df_X.astype(float).values
y = df_y.astype(float).values