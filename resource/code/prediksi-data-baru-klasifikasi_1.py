data = [
    {
        'Customer_Age': 68, 'Gender': 'F', 'Dependent_count': 5,
        'Education_Level': 'Graduate', 'Marital_Status': 'Single',
        'Income_Category': 'Less than $40K', 'Card_Category': 'Blue',
        'Months_on_book': 44, 'Total_Relationship_Count': 6,
        'Months_Inactive_12_mon': 1, 'Contacts_Count_12_mon': 2,
        'Credit_Limit': 8700, 'Total_Revolving_Bal': 800,
        'Avg_Open_To_Buy': 7392, 'Total_Amt_Chng_Q4_Q1': 1.541,
        'Total_Trans_Amt': 1200, 'Total_Trans_Ct': 33,
        'Total_Ct_Chng_Q4_Q1': 3.714, 'Avg_Utilization_Ratio': 0.10,
    },
    {
        'Customer_Age': 50, 'Gender': 'M', 'Dependent_count': 2,
        'Education_Level': 'Graduate', 'Marital_Status': 'Single',
        'Income_Category': '$40K - $60K', 'Card_Category': 'Blue',
        'Months_on_book': 38, 'Total_Relationship_Count': 3,
        'Months_Inactive_12_mon': 2, 'Contacts_Count_12_mon': 0,
        'Credit_Limit': 8077.0, 'Total_Revolving_Bal': 1965,
        'Avg_Open_To_Buy': 6112.0, 'Total_Amt_Chng_Q4_Q1': 0.637,
        'Total_Trans_Amt': 1329, 'Total_Trans_Ct': 26,
        'Total_Ct_Chng_Q4_Q1': 0.444, 'Avg_Utilization_Ratio': 0.243,
    },
]

df_input = pd.DataFrame(data)

# categorical encoding
original_cols = df.drop(['CLIENTNUM', 'Attrition_Flag'], axis=1).columns
df_input = df_input.reindex(columns=original_cols, fill_value=0)

cats = df_input.select_dtypes(include=['object', 'bool']).columns
cat_features = list(cats.values)

label_encoders = {}
for i in cat_features:
    le = LabelEncoder()
    all_unique_values = pd.concat([df_X[i], df_input[i]]).astype(str).unique()
    le.fit(all_unique_values)
    label_encoders[i] = le
    df_input[i] = label_encoders[i].transform(df_input[i].astype(str))

# scaling
df_input = scaler.transform(df_input.astype(float).values)

result = model.predict(df_input)
for i in result:
    int_result = int(i)
    if (int_result == 0):
        decision = 'Existing Customer'
    elif (int_result == 1):
        decision = 'Attrited Customer'
    else:
        decision = 'Not defined'
    print('Result prediction is ', decision)
