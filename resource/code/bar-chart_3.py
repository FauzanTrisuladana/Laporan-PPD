data1 = existing_data['Marital_Status'].value_counts()
data2 = churning_data['Marital_Status'].value_counts()

df_new = pd.concat([data1, data2], keys=['existing', 'attired'], axis=1)

df_new.plot.bar(stacked=True)
plt.title('Marital Status')
plt.ylabel('Count')
plt.show()