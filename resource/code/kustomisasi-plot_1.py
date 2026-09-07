data = df_churning['Customer_Age']
plt.hist(data)
plt.text(60, 1600, "Median Age: " + str(round(data.median(), 2)),
         style='italic', fontsize=10)
plt.text(60, 1800, "Mean Age: " + str(round(data.mean(), 2)),
         style='italic', fontsize=10)
plt.show()