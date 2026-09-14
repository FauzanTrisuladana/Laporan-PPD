# change data format
df_ori = df
df_ori['Date'] = pd.to_datetime(df_ori['Date'])
df_ori['Close'].iloc[:10]