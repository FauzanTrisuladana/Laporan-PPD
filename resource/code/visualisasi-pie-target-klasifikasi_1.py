# cek persentase target class
data = df['Attrition_Flag'].value_counts()
data.plot(kind='pie', autopct='%.2f%%')
plt.show()
