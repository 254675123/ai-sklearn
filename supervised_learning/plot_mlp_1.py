from sklearn.neural_network import MLPClassifier

def mlp_1():
    X = [[0., 0.], [1., 1.]]
    y = [0, 1]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
    model = clf.fit(X, y)
    res = clf.predict([[2., 2.], [-1., -2.]])

    print([coef.shape for coef in clf.coefs_])
    # 预测的概率
    clf.predict_proba([[2., 2.], [1., 2.]])


def mlp_2():
    X = [[0., 0.], [1., 1.]]
    y = [[0, 1], [1, 1]]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes = (15,), random_state = 1)
    clf.fit(X, y)
    # MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
    #               beta_1=0.9, beta_2=0.999, early_stopping=False,
    #               epsilon=1e-08, hidden_layer_sizes=(15,),
    #               learning_rate='constant', learning_rate_init=0.001,
    #               max_iter=200, momentum=0.9, n_iter_no_change=10,
    #               nesterovs_momentum=True, power_t=0.5, random_state=1,
    #               shuffle=True, solver='lbfgs', tol=0.0001,
    #               validation_fraction=0.1, verbose=False, warm_start=False)
    clf.predict([[1., 2.]])
    #array([[1, 1]])
    clf.predict([[0., 0.]])
    #array([[0, 1]])