# visualisasi
y_pred = model.predict(X_test)
print('Accuracy ', accuracy_score(y_test, y_pred))
print('Precision ', precision_score(y_test, y_pred))
print('Recall ', recall_score(y_test, y_pred))
print('Confusion matrix ', confusion_matrix(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=np.unique(y_test)
)
disp.plot(cmap=plt.cm.Blues)
plt.show()
