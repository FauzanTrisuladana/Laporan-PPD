# Visualization

fig1 = plt.figure(figsize=(20,6))
# plotting the result
# because the total number of test is data is high, so we just print the first 100 data
# y_test[0:100] get the first 100 data from y_test or real test data.
# y_pred_mlp is the prediction result from MLP
# y_pred_knn is the prediction result from KNN

plt.plot(y_test, label='Real data')
# plt.plot(y_pred_knn, label='KNN')
# plt.plot(y_pred_dt, label='DT')
plt.plot(y_pred_rf, label='RF')
# plt.plot(y_pred_mlp, label='MLP')

#title
# pyplot.title('First 100 Test Data')
# the x axis is timestamp, with interval 1 day
plt.xlabel('Time t', fontsize=20)
# because we use total rented bikes, so that the y axis is rented bikes
plt.ylabel('rented bikes', fontsize=20)
plt.legend(loc='upper left', fontsize=15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()