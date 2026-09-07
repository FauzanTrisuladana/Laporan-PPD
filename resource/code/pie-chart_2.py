data = df_churning['Marital_Status'].value_counts()

label = data.index

plt.pie(data, labels=label, autopct='%.5f%%')
plt.title('Marital Status')
plt.show()