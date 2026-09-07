data1 = existing_data['Customer_Age']
data2 = churning_data['Customer_Age']

plt.hist(data1, label='existing')
plt.hist(data2, label='churning')
plt.title('Customer Age')
plt.ylabel('Count')
plt.xlabel('age')

plt.legend()
plt.show()