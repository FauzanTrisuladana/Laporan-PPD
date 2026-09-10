data = df['Loan_Status'].value_counts()
data.plot(kind='pie', autopct='%.2f%%')
plt.show()
