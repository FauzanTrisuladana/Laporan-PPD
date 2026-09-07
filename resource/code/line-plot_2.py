df_iot = pd.read_csv('https://raw.githubusercontent.com/FauzanTrisuladana/content/refs/heads/master/datatraining.txt')
df_iot['date'] = pd.to_datetime(df_iot['date'])
df_iot.head()