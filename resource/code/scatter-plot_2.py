ax = existing_data.plot.scatter(x='Customer_Age', y='Months_on_book', label='existing', c='red')
churning_data.plot.scatter(x='Customer_Age', y='Months_on_book', label='churning', ax=ax, c='blue')

plt.title('Customer Age vs months on book')
plt.ylabel('Months on Book')
plt.xlabel('age')

plt.show()