y2 = existing_data['Marital_Status'].value_counts()
y1 = churning_data['Marital_Status'].value_counts()

x1 = np.arange(len(y1.index))
x2 = np.arange(len(y2.index))
bar_width = 0.4

plt.bar(x1, y1, width=bar_width)
plt.bar(x2+bar_width, y2, width=bar_width)

plt.title('Marital Status')
plt.ylabel('Count')
plt.xticks(x2+bar_width/2, labels=df_churning['Marital_Status'].unique())

plt.show()