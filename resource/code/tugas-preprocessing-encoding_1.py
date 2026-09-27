df_task['Operating Airline IATA Code'] = df_task['Operating Airline IATA Code'].fillna('Unknown')
df_task['Published Airline IATA Code'] = df_task['Published Airline IATA Code'].fillna('Unknown')

passenger_col = 'Passenger Count'
if df_task[passenger_col].dtype == 'object':
    df_task[passenger_col] = df_task[passenger_col].str.replace(',', '').astype(float)

categorical_cols = df_task.select_dtypes(include=['object']).columns
le = LabelEncoder()
for col in categorical_cols:
    df_task[col] = le.fit_transform(df_task[col].astype(str))

display(df_task.head())
