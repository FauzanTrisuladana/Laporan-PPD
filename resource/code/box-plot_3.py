data1 = existing_data['Customer_Age'].values
data2 = churning_data['Customer_Age'].values

my_dictionary = {'existing': data1, 'attrited': data2}

plt.violinplot(list(my_dictionary.values()))

plt.title('Customer age')
plt.ylabel('age')
plt.xticks([1, 2], labels=list(my_dictionary.keys()))
plt.show()