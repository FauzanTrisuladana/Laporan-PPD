# Neural Network Model

def mlp (X_train, X_test, y_train, y_test):
    # mlp = multilayer perceptron / neural network for regression.
    # to setup parameter, please refer to = https://scikit-learn.org/stable/modules/generated/sklearn.neural_ne
    mlp_model = MLPRegressor(random_state=42)
    mlp_model = MLPRegressor(hidden_layer_sizes=(100,100, ), max_iter=1000, random_state=42)
    # the model learning from training data
    mlp_model.fit(X_train, y_train)
    # get the prediction output
    y_pred = mlp_model.predict(X_test)
    y_pred = np.round(y_pred, 0)

    # get the root mean square error between prediction and real test data
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    # get the pearson correlation
    corr, p_value = pearsonr(y_test, y_pred)
    # returning the output of RMSE, corr, and prediction result
    return rmse, corr, y_pred