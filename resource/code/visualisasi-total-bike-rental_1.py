# Visualization Total Bike Rental

fig1 = plt.figure(figsize=(20,6))
plt.plot(df_new['cnt'])
#plt.xlabel('Time t',  fontsize=20)
#because we use temperature data, so that the y axis is temperature
plt.ylabel('# total rented bikes',  fontsize=20)
plt.legend(loc='upper left',  fontsize=15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()