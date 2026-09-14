# Visualization Total Bike Rental

fig1 = plt.figure(figsize=(20,6))
plt.plot(df_new['Close'])
plt.xlabel('Day',  fontsize=20)
plt.ylabel('Closing price',  fontsize=20)
plt.legend(loc='upper left',  fontsize=15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()