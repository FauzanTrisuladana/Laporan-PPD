data1 = existing_data['Customer_Age']
data2 = churning_data['Customer_Age']
df_new = pd.concat([data1, data2], keys=['existing', 'attrited'], axis=1)

df_new.plot.box() # Bisa pakai cara ini
# df_new.plot(kind='box') # Bisa menggunakan cara ini juga

plt.title('Customer age')
plt.ylabel('age')
plt.show()