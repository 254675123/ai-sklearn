

def fs_1():
    from sklearn.feature_selection import VarianceThreshold
    X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
    sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
    res = sel.fit_transform(X)

    # array([[0, 1],
    #        [1, 0],
    #        [0, 0],
    #        [1, 1],
    #        [1, 0],
    #        [1, 1]])

def fs_2():
    from sklearn.datasets import load_iris
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2
    iris = load_iris()
    X, y = iris.data, iris.target
    print(X.shape) # (150, 4)
    X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
    print(X_new.shape)  # (150, 2)

def fs_3():
    from sklearn.svm import LinearSVC
    from sklearn.datasets import load_iris
    from sklearn.feature_selection import SelectFromModel
    iris = load_iris()
    X, y = iris.data, iris.target
    print(X.shape)
    #(150, 4)
    lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X, y)
    model = SelectFromModel(lsvc, prefit=True)
    X_new = model.transform(X)
    print(X_new.shape)
    #(150, 3)

fs_3()