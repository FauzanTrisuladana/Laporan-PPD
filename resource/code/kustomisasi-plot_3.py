data1 = existing_data['Customer_Age']
data2 = churning_data['Customer_Age']

plt.hist(data1, label='Existing customer')
plt.hist(data2, label='Attrited customer')

plt.title('Customer Age')
plt.ylabel('Count')
plt.xlabel('Age')

plt.legend()
plt.show()