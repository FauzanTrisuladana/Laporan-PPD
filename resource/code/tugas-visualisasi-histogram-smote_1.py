dfx_ori = pd.DataFrame(X_train, columns=df_X.columns)
dfy_ori = pd.DataFrame(y_train.values, columns=['Occupancy'])
df_sebelum = pd.concat([dfx_ori, dfy_ori], axis=1)

dfx_res = pd.DataFrame(X_resampled, columns=df_X.columns)
dfy_res = pd.DataFrame(y_resampled.values, columns=['Occupancy'])
df_sesudah = pd.concat([dfx_res, dfy_res], axis=1)

f, axes = plt.subplots(1, 2, figsize=(10, 6))
sns.histplot(data=df_sebelum, x='Temperature', hue='Occupancy', ax=axes[0]).set(title='Sebelum')
sns.histplot(data=df_sesudah, x='Temperature', hue='Occupancy', ax=axes[1]).set(title='Sesudah')
plt.xticks()
plt.show()
