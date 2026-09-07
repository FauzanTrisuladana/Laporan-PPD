y1 = churning_data['Months_on_book']
x1 = churning_data['Customer_Age']

y2 = existing_data['Months_on_book']
x2 = existing_data['Customer_Age']

plt.scatter(x1, y1, label='churning')
plt.scatter(x2, y2, label='existing')
plt.title('Customer Age vs months on book')
plt.ylabel('Months on Book')
plt.xlabel('age')

plt.legend()
plt.show()